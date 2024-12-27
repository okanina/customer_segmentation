import os
from pathlib import Path


list_of_files =[
    ".github/workflow/.gitkeep",
    "src/__init__.py",
    "src/pcomponents/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils.py",
    "src/logger.py",
    "src/exception.py",
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