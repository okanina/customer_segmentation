import yaml
import sys
import os
import dill
import pickle
from ensure import ensure_annotations
from box import ConfigBox
from src.exception import CustomException
from pathlib import Path

@ensure_annotations
def read_yaml(yaml_path: Path):
    try:
        with open(yaml_path, 'r') as yaml_file:
            content =yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e, sys)

@ensure_annotations
def write_yaml(file_path, content):
    try:
        with open(file_path, "w") as f:
            yaml.dump(content, f, default_flow_style=False) 
    except Excption as e:
        raise CustomException(e, sys)

@ensure_annotations
def create_directories(directory_path: list):
    try:
        for path in directory_path:
            os.makedirs(path, exist_ok=True)
    except Exception as e:
        raise CustomException(e, sys)

@ensure_annotations
def save_obj(file_path, obj):
    try:
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            file_obj.close()
    except Exception as e:
        raise CustomException(e, sys)

@ensure_annotations
def load_binary_files(filepath):
    try:
        with open(filepath, "rb") as f:
            obj = pickle.load(f)
        return obj    
    except Exception as e:
        raise CustomException(e, sys)

@ensure_annotations
def save_file(file_name, obj):
    try:
        with open(file_name, "w") as f:
            json.dump(obj, f)
        # return obj    
    except Exception as e:
        raise CustomException(e, sys)
