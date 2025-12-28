import os
from pathlib import Path


list_of_files =[
    ".github/workflow/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/data_validation.py",
    "src/components/data_clustering.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/components/model_pusher.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/entity/__init__.py",
    "src/entity/artifact_entity.py",
    "src/entity/config_entity.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/constant/__init__.py",  
    "src/logger.py",
    "src/exception.py",
    "config.yaml",
    "params.yaml",
    "schema.yaml",
    "setup.py",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)

    #creating a directory if it does not exist.
    if filedir !='':
        os.makedirs(filedir, exist_ok=True)

    #creating a file in path.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass