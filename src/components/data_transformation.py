import sys
import pandas as pd
import numpy as np
from src.utils.common import save_obj
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from category_encoders import OneHotEncoder
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

        Description: The method transform columns into a numpy array.

        Output     : Returns an artifact.

        Failure    : writes log and raise an exception
        """
        try:
            df= pd.read_csv(self.artifact.local_data_file_path)
            df.drop(columns = ["customer_id"], inplace=True)
            
            num_pipeline = Pipeline(steps =[
                                            ("impute", SimpleImputer(strategy="mean")),
                                            ("std", StandardScaler()),
                                            ]
                                    )

            cat_pipeline= Pipeline(steps =[
                                            ("ohe", OneHotEncoder())
                                        ]
                                    )

            processor = ColumnTransformer([
                                            ("num_pipeline", num_pipeline, df.select_dtypes("number").columns.to_list()),
                                            ("cat_pipeline", cat_pipeline, df.select_dtypes("object").columns.to_list())
                                          ]
                                        )
            transformed_train_input = processor.fit_transform(df)
            

            logging.info("Column transformation complete.")

            np.save(self.config.transformed_local_file_path.replace("csv", "npy"), transformed_train_input)

            save_obj(self.config.transformer_object_file_path, processor)

            logging.info("train array and preprocessor object successfully saved.")

            data_transformation_artifact = DataTransformationArtifact(transformed_local_file_path=self.config.transformed_local_file_path,
                                                                      transformer_object_file_path=self.config.transformer_object_file_path)
            return data_transformation_artifact
        except Exception as e:
            raise CustomException(e, sys)
