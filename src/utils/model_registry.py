from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

MODEL_REGISTRY = {
                "RandomForestClassifier": RandomForestClassifier(),
                "XGBClassifier": XGBClassifier(),
                "LogisticRegression": LogisticRegression(),
                "DecisionTreeClassifier": DecisionTreeClassifier()
                }