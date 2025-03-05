from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    local_data_file_path: Path
    train_file_path: Path
    test_file_path: Path

@dataclass
class DataValidationArtifact:
    drift_report_file_path: Path

@dataclass
class DataTransformationArtifact:
    transformed_train_file_path: Path
    transformed_test_file_path: Path
    transformer_object_file_path: Path


