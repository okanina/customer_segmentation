import os
import sys
import pickle
import numpy as np
from src.utils.common import load_binary_files
from sklearn.metrics import accuracy_score, classification_report
from src.entity.config_entity import ModelEvaluationConfig
from src.entity.artifact_entity import ModelTrainerArtifact


class ModelEvaluation:
    def __init__(self, artifact:ModelTrainerArtifact,
                       config:ModelEvaluationConfig):

        self.artifact = artifact
        self.config = config
 
     
    def initiate_model_evaluation(self):

        test_arr = np.load(self.artifact.target_test_file_path)
        processor = load_binary_files(self.artifact.transformer_object_file_path)
        model = load_binary_files(self.artifact.trained_model_file_path)

       
        X_test, y_test = test_arr[:,: -1], test_arr[:,-1]

        y_pred = model.predict(X_test)

        accuracy =accuracy_score(y_test, y_pred)

        with open(self.config.metrics_file_path, "w") as f:

            original_stdout = sys.stdout
            sys.stdout = f
            print("Accuracy score:", accuracy)
            print("Classification Report:\n", classification_report(y_test, y_pred))
            sys.stdout = original_stdout

        

    
