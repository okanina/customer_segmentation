import pandas as pd
from src.persistence.database import upsert_historic
from src.config.configuration import configurationManager


config= configurationManager()
data_ingestion_config = config.get_data_ingestion_config()

def run_historic_upsert():

    """
    updating the database with labels.
    """
    df = pd.read_csv(data_ingestion_config.local_data_file_path)        

    labels = pd.read_csv("artifact/data_clustering/labels.csv")

    upsert_historic(labels, df)

if __name__=="__main__":
    run_historic_upsert()