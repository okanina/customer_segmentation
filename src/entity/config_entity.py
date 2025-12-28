from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str
    local_data_file_path: Path
    test_file_path: Path
    train_test_split_ratio: float
    database_name: str
    collection_name: str

@dataclass
class DataValidationConfig:
    data_validation_dir: str
    drift_report_file_path: Path
    COLUMNS: dict
    numerical_columns: dict
    categorical_columns: dict
    id_column: str

@dataclass
class DataTransformationConfig:
    data_transformation_dir: str
    transformed_local_file_path: Path
    transformer_object_file_path: Path

@dataclass
class DataClusteringConfig:
    data_clustering_dir: str
    target_train_file_path: Path
    target_test_file_path: Path
    clusters_file_path: Path

@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str
    trained_model_file_path: Path
    models: dict  

@dataclass
class ModelEvaluationConfig:
    model_evaluation_dir: str
    metrics_file_path: Path

