import os
import sys
import pickle
import pandas as pd
from pandas import DataFrame
from src.logger import logging
from src.exception import CustomException
from pymongo import MongoClient
from dotenv import load_dotenv
from src.utils.common import save_file
from src.config.configuration import configurationManager

load_dotenv(".venv")

config= configurationManager()
data_ingestion_config =config.get_data_ingestion_config() 
        

def database_authentication():      

    try:
        login_username = os.environ.get("login_username")
        login_password = os.environ.get("login_password")
            
        if not login_username or not login_password:
            raise RuntimeError("Your database login credentials is incorrect. Pleasee double check and log in again.")

        client = MongoClient(f"mongodb+srv://{login_username}:{login_password}@cluster0.xtxfmd5.mongodb.net/")

        database = client[data_ingestion_config.database_name]
        
        collection = database[data_ingestion_config.collection_name]

        return collection

    except Exception as e:
        raise CustomException(e, sys)


def upsert_historic(labels, df:DataFrame):

    collection = database_authentication()    
    
    try:
        n = 0
        n_modified = 0
        
        df["cluster_labels"] = labels.values

        for obs in df.to_dict(orient = "records"): 
            obs["Customer ID"] = obs.pop("customer_id")
            result = collection.update_one(
                                filter = {"Customer ID": obs["Customer ID"]},
                                update ={"$set":{"cluster_labels":obs["cluster_labels"]}},
                                upsert = True
                                )
           
            n+=result.matched_count

            n_modified += result.modified_count
            

        transacton_result = {"Number of matched documents":n, "and number of modified": n_modified}

        logging.info(transacton_result)

    except Exception as e:
        raise CustomException(e, sys)

def upsert_live_cluster(cluster_label, customer_id):

    collection = database_authentication()    
    
    try:
        n = 0
        n_modified = 0

        result = collection.update_one(
                                filter = {"Customer ID": customer_id},
                                update ={"$set":{"cluster_labels":int(cluster_label)}},
                                upsert = False
                                )
           
        n+=result.matched_count

        n_modified += result.modified_count            

        transacton_result = {"Number of matched documents":n, "and number of modified": n_modified}

        logging.info(transacton_result)

    except Exception as e:
        raise CustomException(e, sys)

