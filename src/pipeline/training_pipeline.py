import sys
from pathlib import Path
from src.logger import logging
from src.exception import CustomException
from src.config.configuration import configurationManager
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer
# from src.components.model_evaluation import ModelEvaluation


class TrainPipeline:
    def __init__(self):
        self.config= configurationManager()

    def start_data_ingestion(self):

        logging.info(">>>>>>>>>>>>Data Ingestion Initiated.<<<<<<<<<<<")

        try:
            data_ingestion_config = self.config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config =data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info(">>>>>>>>>>>>Data Ingestion Completed.<<<<<<<<<<<.\n")

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys)

    def start_data_validation(self, data_ingestion_artifact):

        logging.info(">>>>>>>>>>>>Data Validation Initiated.<<<<<<<<<<<")

        try:
            data_validation_config = self.config.get_data_validation_config()
            data_validation =DataValidation(config=data_validation_config,
                                            artifact =data_ingestion_artifact)
            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info(">>>>>>>>>>>>Data Validation Complete.<<<<<<<<<<<<<.\n")

            return data_validation_artifact
        except Exception as e:
            raise CustomException(e, sys)

    def start_data_transformation(self, path:Path, artifact):

        logging.info(">>>>>>>>>>>>Data Transformation Initiated.<<<<<<<<<<<")

        try:
            with open(path, "r") as f:
                status =f.read().split(" ")[-1]
                
                if status == "True":
                    data_transformation_config = self.config.get_data_transformation_config()
                    data_transformation = DataTransformation(config = data_transformation_config, artifact = artifact)
                    data_transformation_artifact=data_transformation.initiate_data_transformation()
                    
                    logging.info(">>>>>>>>>>>>>Data Transformation Complete.<<<<<<<<<<<<<.\n")

                    return data_transformation_artifact
        except Exception as e:
            raise CustomException(e, sys)

    # def start_model_trainer(self):

    #     logging.info(">>>>>>>>>>>>Model Trainer Initiated.<<<<<<<<<<<")

    #     try:
    #         pass
    #     except Exception as e:
    #         raise customException(e, sys)

    # def start_model_evaluation(self):

    #     logging.info(">>>>>>>>>>>>Model Evaluation Initiated.<<<<<<<<<<<")

    #     try:
    #         pass
    #     except Exception as e:
    #         raise CustomException(e, sys)

    def run_pipeline(self):

        logging.info(">>>>>>>>>>>>Run Pipeline Initiated.<<<<<<<<<<<")

        try:
            data_ingestion_artifact =self.start_data_ingestion()
            data_validation_artifact =self.start_data_validation(data_ingestion_artifact)
            data_transformation_artifact =self.start_data_transformation(data_validation_artifact.drift_report_file_path, 
                                                                         artifact = data_ingestion_artifact)
            logging.info(">>>>>>>>>>>>Run Pipeline Completed.<<<<<<<<<<<")
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    pipeline =TrainPipeline()
    pipeline.run_pipeline()