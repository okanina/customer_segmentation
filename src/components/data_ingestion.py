import sys
import os 
import numpy as np
import pandas as pd
from pandas import DataFrame
from src.logger import logging
from src.exception import CustomException
from astrapy import DataAPIClient
from sklearn.model_selection import train_test_split
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from dotenv import load_dotenv
load_dotenv(".venv")


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):

        self.config=config


    def export_collection_to_dataframe(self, collection_name:str)->DataFrame:
        """
        Method Name: export_collection_to_dataframe

        Description: The method export an entire collection from the database then saves it locally.

        Output     : Returns a DataIngestionArtifact.

        Failure    : writes log and raise an exception
        """

        logging.info("Extracting data froma a database.")

        try:

            endpoint = os.environ.get("endpoint")
            token = os.environ.get("authToken")

            if not endpoint or not token:
                raise RuntimeError("Environment variable API_ENDPOINT and APPLICATION_TOKEN must be defined.")

            client = DataAPIClient(token)
            
            database_name = client.get_database_by_api_endpoint(endpoint)

            collection = database_name.get_collection(collection_name)
            
            df = pd.DataFrame(list(collection.find(projection={"_id": False, "CUST_ID": False})))
           
            df.replace({"na":np.nan}, inplace=True)

            df.to_csv(self.config.local_data_file_path, index=False)

            return df

        except Exception as e:
            raise CustomException(e, sys)


    def split_data_to_train_test(self, df:DataFrame):

        """
        Method Name: split_data_to_train_test

        Description: The method splits a dataframe into train and test sets.

        Output     : Returns a tuple.

        Failure    : writes log and raise an exception
        """

        logging.info("Splitting data into train test set.")

        try:
            
            train_df, test_df = train_test_split(df, test_size=self.config.train_test_split_ratio, random_state=42)

            train_df.to_csv(self.config.train_file_path, index=False)

            test_df.to_csv(self.config.test_file_path, index=False)

            logging.info("train and test set saved successful.")

            
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self)->DataIngestionArtifact:

        try:
            if not os.path.exists(self.config.local_data_file_path):
                df = self.export_collection_to_dataframe(collection_name = self.config.collection_name)
                self.split_data_to_train_test(df)
                logging.info("Collection extraction completed.")

            else:
                logging.info("Collecton has already been saved locally.")

                        
            data_ingestion_artifact = DataIngestionArtifact(local_data_file_path = self.config.local_data_file_path,
                                                            train_file_path = self.config.train_file_path,
                                                            test_file_path =self.config.test_file_path
                                                            )

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys)
                       


            