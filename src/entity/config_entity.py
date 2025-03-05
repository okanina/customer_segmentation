from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str
    local_data_file_path: Path
    train_file_path: Path
    test_file_path: Path
    train_test_split_ratio: float
    collection_name: str

@dataclass
class DataValidationConfig:
    data_validation_dir: str
    drift_report_file_path: Path
    ALL_SCHEMA: dict


@dataclass
class DataTransformationConfig:
    data_transformation_dir: str
    train_file_path: Path
    test_file_path: Path
    transformer_object_file_path: Path

@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str
    trained_model_file_path: Path
    

@dataclass
class ModelEvaluationConfig:
    model_evaluation_dir: Path
    metrics_file: Path

