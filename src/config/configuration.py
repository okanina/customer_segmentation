from src.entity.config_entity import (DataIngestionConfig,
                                      DataValidationConfig,
                                      DataTransformationConfig,
                                      ModelTrainerConfig,
                                      ModelEvaluationConfig
                                     )
from src.utils.common import read_yaml, create_directories
from src.constant import *

class configurationManager:
    def __init__(self, 
                config_filepath = CONFIG_FILE_PATH, 
                params_filepath = PARAMS_FILE_PATH,
                schema_file_path = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:

        config = self.config.data_ingestion
        params = self.params

        create_directories([config.data_ingestion_dir])

        data_ingestion_config = DataIngestionConfig(data_ingestion_dir = config.data_ingestion_dir,
                                                    local_data_file_path = config.local_data_file_path,
                                                    train_file_path = config.train_file_path,
                                                    test_file_path = config.test_file_path,
                                                    collection_name = config.collection_name,
                                                    train_test_split_ratio = params.train_test_split_ratio)
        
        return data_ingestion_config

    def get_data_validation_config(self)->DataValidationConfig:

        config =self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.data_validation_dir])

        data_validation_config = DataValidationConfig(
                                                    data_validation_dir = config.data_validation_dir,                                                 
                                                    drift_report_file_path = config.drift_report_file_path,
                                                    ALL_SCHEMA =schema
                                                   )

        return data_validation_config

    def get_data_transformation_config(self)->DataTransformationConfig:

        config = self.config.data_transformation

        create_directories([config.data_transformation_dir])

        data_transformation_config = DataTransformationConfig(
                                                            data_transformation_dir = config.data_transformation_dir,
                                                            train_file_path = config.train_file_path,
                                                            test_file_path = config.test_file_path,
                                                            transformer_object_file_path = config.transformer_object_file_path
                                                            )

        return data_transformation_config

    def get_model_trainer_config(self):

        config = self.config.model_trainer

        create_directories([config.model_trainer_dir])

        model_trainer_config = ModelTrainerConfig(
                                                model_trainer_dir = config.model_trainer_dir,
                                                trained_model_file_path = config.trained_model_file_path
                                               )
                                            
        return model_trainer_config


    def get__evaluation_config(self):
        config = self.config.model_evaluation

        create_directories([config.data_evaluation_dir])

        model_evaluation_config = ModelEvaluationConfig(model_evaluation_dir = config.model_evaluation_dir,
                                                        metrics_file = config.etrics_file
                                                        )

        return model_evaluation_config



        


        