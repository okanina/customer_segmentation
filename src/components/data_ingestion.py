import sys
import os 
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from pymongo import MongoClient
from src.persistence.database import database_authentication
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from dotenv import load_dotenv
load_dotenv(".venv")


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):

        self.config=config

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        """
        Method Name: export_collection_to_dataframe

        Description: This method export an entire collection from a database in the cloud then saves it locally.

        Output     : Returns a DataIngestionArtifact.

        Failure    : writes log and raise an exception
        """

        logging.info("Extracting data from a database.")

        try:
            collection = database_authentication()
            
            df = pd.DataFrame(                              
                collection.find({},
            {
            "_id": 0,
            "Customer ID": 1,
            "Gender": 1,
            "Age": 1,
            "City": 1,
            "Membership Type": 1,
            "Total Spend": 1,
            "Items Purchased": 1,
            "Average Rating": 1,
            "Discount Applied": 1,
            "Days Since Last Purchase": 1,
            "Satisfaction Level": 1
        }))

            df.rename(columns={"Customer ID":"customer_id", 
                                "Gender":"gender",
                                "Age":"age",
                                "City":"city",
                                "Membership Type":"membership_type",
                                "Total Spend":"total_spend",
                                "Items Purchased":"items_purchased",
                                "Average Rating":"average_rating",
                                "Discount Applied":"discount_applied",
                                "Days Since Last Purchase":"days_since_last_purchase",
                                "Satisfaction Level":"satisfaction_level"}, inplace=True)
           
            df.replace({"na":np.nan}, inplace=True)

            df.to_csv(self.config.local_data_file_path, index=False)

            data_ingestion_artifact = DataIngestionArtifact(local_data_file_path = self.config.local_data_file_path)

            return data_ingestion_artifact            

        except Exception as e:
            raise CustomException(e, sys)    