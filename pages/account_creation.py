import os
import random
import numpy as np
import pandas as pd
import streamlit as st
from pymongo import MongoClient
from src.logger import logging
from src.pipeline.prediction_pipeline import *
from src.pipeline.prediction_pipeline import CustomerData
from dotenv import load_dotenv
from src.persistence.database import database_authentication, upsert_live_cluster


collection = database_authentication()

def get_data():

    df = pd.read_csv("artifact/data_ingestion/customer_segmentation.csv")

    customer_id = df["customer_id"].iloc[-1] +1
    gender = st.selectbox('Select your genser', df["gender"].unique())
    age = st.number_input('Enter your age', min_value = 18, max_value = 80)
    city = st.selectbox('Select your city', df['city'].unique())
    membership_type  = st.selectbox('Select your membership type', df["membership_type"].unique())
    amounts =pd.Series(
        df["total_spend"]
        .squeeze()
    )
    
    total_spend = np.random.choice(amounts)

    if total_spend>0:
        items_purchased = random.randint(0, df["items_purchased"].max())
        average_rating = df["average_rating"].mean()
        discount_applied = np.random.choice([True, False])
        days_since_last_purchase = random.randint(0, df["days_since_last_purchase"].max())
        satisfaction_level = df["satisfaction_level"].mode().iloc[0]

    else:
        items_purchased = 0
        average_rating = np.nan
        discount_applied = False
        days_since_last_purchase = 0
        satisfaction_level = np.nan

    data = CustomerData(
            # customer_id = customer_id,
            gender = gender,
            age = age,
            city = city,
            membership_type = membership_type,
            total_spend = total_spend,
            items_purchased = items_purchased,
            average_rating = average_rating,
            discount_applied = discount_applied,
            days_since_last_purchase = days_since_last_purchase,
            satisfaction_level = satisfaction_level
        )

    df = data.data_to_frame()

    return df 

with st.form("account creation"):

    pred = PredictionPipeline()
    df = get_data()     
     
    if st.form_submit_button("create account"):    
               
        cluster_pred = pred.get_predictions(df)

        new_col = {}

        for col in df.columns.to_list():

            parts =[]

            if "_" in col:
                col_split = col.split("_")
                    # print(col_split)
                for word in col_split:                    
                    parts.append(word.capitalize())
                new_col[col] = " ".join(parts)
            else:
                new_col[col] = col.capitalize()
            
            new_col["customer_id"] = "Customer ID"
                               
        df.rename(columns= new_col, inplace=True)  
     
        if "customer_id" not in df.columns:
            last_doc = collection.find_one(
                            filter={},
                            sort = [("Customer ID", -1)]
                            )
            df["Customer ID"] = last_doc["Customer ID"] + 1             
        
        collection.insert_one(df.iloc[0].to_dict())

        logging.info("One document was successfully inserted.") 
   
        upsert_live_cluster(cluster_pred, int(df["Customer ID"].iloc[0]))

        logging.info(f"Successfully updated document: {df['Customer ID'].iloc[0]} with cluster {cluster_pred}.")

        st.write("Congratualtions! your account was successfully created.")


