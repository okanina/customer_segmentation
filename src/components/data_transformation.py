import sys
import pandas as pd
import numpy as np
from src.utils.common import save_obj
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact

class DataTransformation:
    def __init__(self, config: DataTransformationConfig,
                       artifact:DataIngestionArtifact):

        self.config = config
        self.artifact = artifact           

    def initiate_data_transformation(self):
        """
        Method Name: initiate_data_transformation

        Description: The method transform columns.

        Output     : Returns an artifact.

        Failure    : writes log and raise an exception
        """
        try:
            train_df= pd.read_csv(self.artifact.train_file_path)
            test_df= pd.read_csv(self.artifact.test_file_path)

            num_pipeline = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")),
                                                ("scaler", StandardScaler())
                                                ])
            preprocessor = ColumnTransformer([("num_pipeline",num_pipeline, train_df.select_dtypes("number").columns.to_list())])

            transformed_train_input = preprocessor.fit_transform(train_df)
            transformed_test_input = preprocessor.transform(test_df)

            logging.info("Column transformation complete.")

            np.save(self.config.train_file_path.replace("csv", "npy"), transformed_train_input)
            np.save(self.config.test_file_path.replace("csv", "npy"), transformed_test_input)
            save_obj(self.config.transformer_object_file_path, preprocessor)

            logging.info("train array, test array and preprocessor object successfully saved.")

            data_transformation_artifact = DataTransformationArtifact(train_file_path=self.config.train_file_path,
                                                                      test_file_path =self.config.test_file_path,
                                                                      transformer_object_file_path=self.config.transformer_object_file_path)
            return data_transformation_artifact
        except Exception as e:
            raise CustomException(e, sys)
