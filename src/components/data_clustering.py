import sys
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.cluster import KMeans
from src.entity.artifact_entity import DataTransformationArtifact, DataClusteringArtifact
from src.entity.config_entity import DataClusteringConfig

class DataClustering:
    def __init__(self, artifact: DataTransformationArtifact,
                       config: DataClusteringConfig):

        self.artifact = artifact
        self.config = config

    def initiate_data_clustering(self):

        """
        Method Name: initiate_data_clustering.

        Description: Create clusters to form a target column on a trainset which will be used for classification later on.

        Output: Returns the train set with a target column.

        Failure: Raises a custom Exception.
        """

        try:
            #loading a numpy file.
            train_arr = np.load(self.artifact.transformed_local_file_path)

            model = KMeans(n_clusters=6, random_state = 42)
            model.fit(train_arr)

            logging.info("Clustering complete.")

            labels = model.labels_
            df = pd.DataFrame({"cluster_labels": labels})
                      
            indices = np.random.permutation(len(train_arr))
            split_index = int(len(train_arr) * 0.8)

            X_train = train_arr[indices[:split_index]]
            y_train = labels[indices[:split_index]]
            
            X_test = train_arr[split_index:]
            y_test = labels[split_index:]  

            train_array = np.c_[X_train,y_train]
            test_array = np.c_[X_test, y_test]          

            df.to_csv(self.config.clusters_file_path, index=False)
            np.save(self.config.target_test_file_path, test_array)            
            np.save(self.config.target_train_file_path, train_array)


            logging.info("clusters assigned to the training set and labels saved.")

            data_clustering_artifact = DataClusteringArtifact(target_train_file_path = self.config.target_train_file_path,
                                                              target_test_file_path= self.config.target_test_file_path,
                                                              transformer_object_file_path = self.artifact.transformer_object_file_path)

            return data_clustering_artifact

        except Exception as e:
            raise CustomException(e, sys)



