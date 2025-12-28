import pandas as pd 
from src.entity.artifact_entity import ModelTrainerArtifact 
from src.utils.common import load_binary_files 
from src.components.data_validation import DataValidation 
from src.config.configuration import *

class PredictionPipeline: 
    def __init__(self):
        pass

        # self.validation = validation

    def get_predictions(self, features): 

        # self.validation.initiate_data_validation() 
        processor= load_binary_files("artifact/data_transformation/preprocessor.pkl") 
        model = load_binary_files("artifact/model_trainer/model.pkl") 
        scaled_features = processor.transform(features) 
        y_pred = model.predict(scaled_features) 
        return y_pred

class CustomerData: 
    def __init__(self,gender, age, city, membership_type, total_spend, items_purchased, average_rating, discount_applied, days_since_last_purchase, satisfaction_level): 

        self.gender = gender 
        self.age = age 
        self.city = city 
        self.membership_type = membership_type 
        self.total_spend = total_spend 
        self.items_purchased = items_purchased 
        self.average_rating = average_rating 
        self.discount_applied = discount_applied 
        self.days_since_last_purchase = days_since_last_purchase 
        self.satisfaction_level = satisfaction_level

    def data_to_frame(self): 

        input_data ={"gender": [self.gender], 
                        "age": [self.age], 
                        "city": [self.city], 
                        "membership_type": [self.membership_type], 
                        "total_spend":[self.total_spend], 
                        "items_purchased": [self.items_purchased], 
                        "average_rating": [self.average_rating], 
                        "discount_applied": [self.discount_applied], 
                        "days_since_last_purchase": [self.days_since_last_purchase], 
                        "satisfaction_level":[self.satisfaction_level] 
                        } 
        df = pd.DataFrame(input_data)
        
        return df