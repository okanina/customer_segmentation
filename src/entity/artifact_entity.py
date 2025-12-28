from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    local_data_file_path: Path   
    

@dataclass
class DataValidationArtifact:
    drift_report_file_path: Path

@dataclass
class DataTransformationArtifact:
    transformed_local_file_path: Path
    transformer_object_file_path: Path

@dataclass
class DataClusteringArtifact:
    target_train_file_path: Path
    target_test_file_path: Path
    transformer_object_file_path: Path

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: Path
    target_test_file_path: Path
    transformer_object_file_path: Path


