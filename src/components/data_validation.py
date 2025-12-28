import sys
import json
import pandas as pd
from pandas import DataFrame
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from evidently.future.report import Report
from evidently.future.metrics import *
from evidently.future.presets import *
from evidently.future.presets import DataSummaryPreset, DataDriftPreset
from evidently.future.datasets import Dataset
from evidently.future.datasets import DataDefinition


class DataValidation:
    def __init__(self, config:DataValidationConfig,
                       artifact: DataIngestionArtifact):

        self.config = config
        self.artifact = artifact

    def validate_columns_schema(self, df:DataFrame)->bool:
        """
        Method Name: validate_columns_schema

        Description: The method validate columns of a dataframe.

        Output     : Returns a boolean values.

        Failure    : writes log and raise an exception
        """

        logging.info("Validating Train set and Test set columns.")

        try:
            validate_status = None

            all_columns = df.columns.to_list()
            schema_columns = self.config.COLUMNS        

            for col in all_columns:
                if (col not in schema_columns.keys()) or (df[col].dtype != (int or float or object or bool)):
                    validate_status = False                   
                else:
                    validate_status = True
                    
            return validate_status
  
        except Exception as e:
            raise CustomException(e, sys)

    
    def detect_data_drift(self, reference_df: DataFrame, current_df:DataFrame)->bool:

        """
        Method Name: detect_data_drift.

        Description: This method detect the schema of the columns and see if there's a data drift on the incoming data.

        Output     : Returns a boolean value.

        Failure    : writes log and raise an exception
        """
        try:    
                 
            schema= DataDefinition(id_column = list(self.config.id_column.keys())[0],
                                  numerical_columns=list(self.config.numerical_columns.keys()),
                                  categorical_columns=list(self.config.categorical_columns.keys()))
                      
            eval_data_1 = Dataset.from_pandas(pd.DataFrame(current_df), data_definition=schema)
           
            eval_data_2 = Dataset.from_pandas(pd.DataFrame(reference_df), data_definition=schema)                 

            report = Report(metrics=[DataDriftPreset()],
                                     include_tests=True)
            my_eval = report.run(eval_data_1, eval_data_2)
            report = my_eval.json()
            json_report = json.loads(report)
            for key in json_report['tests']:
                if json_report['tests'][key]['status']=="SUCCESS":
                    validate_status=False
                else:
                    validate_status=True
         
            return validate_status

        except Exception as e:
            raise CustomException(e, sys)
   
    def initiate_data_validation(self):
        try:  
            # print(self.artifact.train_file_path)
            train_df = pd.read_csv(self.artifact.train_file_path)                       

            train_validate_status= self.validate_columns_schema(train_df)
            test_validate_status = self.validate_columns_schema(test_df)

            drift_status = self.detect_data_drift(train_df, test_df)
            
            if (train_validate_status is True and 
            #    test_validate_status is True and
               drift_status is False):

               validate_status= True
               with open(self.config.drift_report_file_path, "w") as f:
                f.write(f"Validation Status is {validate_status}")

            else:

                validate_status = False
                with open(self.config.drift_report_file_path, "w") as f:
                    f.write(f"Validation Status is {validate_status}")
            
            logging.info(f"Validation status is {validate_status}.")
                    
            data_validation_artifact = DataValidationArtifact(drift_report_file_path = self.config.drift_report_file_path)

            return data_validation_artifact

        except Exception as e:
            raise CustomException(e, sys)