import sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.utils.common import save_obj
from src.exception import CustomException
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from src.utils.model_registry import MODEL_REGISTRY
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from src.entity.artifact_entity  import DataClusteringArtifact, ModelTrainerArtifact
from src.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig,
                       artifact: DataClusteringArtifact):
        
        self.config = config
        self.artifact =artifact

    def initiate_model_trainer(self):
        """
        Name: initiate_model_trainer

        Description: Clustering is done.This method trains a classifier model.

        Output: 

        Failure: It raise an exception and writes a log.

        """

        scores_report = {}
        trained_models = {}

        models = self.config.models

        try:
            train_arr = np.load(self.artifact.target_train_file_path)
            
            X_train, y_train = train_arr[:,:-1], train_arr[:, -1]

            # import models.
            for model_name, param in models.items():

                model = MODEL_REGISTRY[model_name]
                gs = GridSearchCV(estimator=model, param_grid = param, cv=3, return_train_score=True)
                gs.fit(X_train, y_train)

                model.set_params(**gs.best_params_)
                model.fit(X_train, y_train)

                # predictions
                y_train_pred = model.predict(X_train)

                train_score = accuracy_score(y_train, y_train_pred)

                scores_report[model_name] = train_score 
                trained_models[model_name] = model

            logging.info("Model training completed.") 


            best_model_name= max(scores_report, key =scores_report.get)
            best_model_score = scores_report[best_model_name]
            best_model = trained_models[best_model_name] 

            if  best_model_score < 0.8:
                raise Exception("No best model found!")
            
            logging.info(f"Best model:{best_model} and it score: {best_model_score}")

            logging.info(f"The best model is {best_model_name}.")

            save_obj(self.config.trained_model_file_path, best_model)

            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path = self.config.trained_model_file_path,
                                                          target_test_file_path = self.artifact.target_test_file_path,
                                                          transformer_object_file_path=self.artifact.transformer_object_file_path)

            return model_trainer_artifact
            
        except Exception as e:
            raise CustomException(e, sys)
        