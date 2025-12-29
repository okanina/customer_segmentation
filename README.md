## Analysis of Customer Behaviour and Segmentation (In Progress)

## Project Overview

This project focuses on exploring customer engagement and purchasing patterns.  
The goal is to segment customers into clusters based on their behavioural and demographic attributes.

---

## Project Objectives & Approach

* **Data Cleaning and Transformation:**  
  Handle missing values and apply one-hot encoding to categorical variables.

* **Feature Engineering:**  
  Prepare meaningful features from transactional and demographic data.

* **Data Preprocessing:**  
  Apply feature scaling and encoding to standardize the dataset and improve the clustering process.

* **Customer Segmentation using KMeans Clustering:**  
  Segment customers into distinct groups using K-Means clustering to enable targeted marketing and personalization.

* **Cluster Replication using Classification Models:**  
  Train supervised classification models on cluster labels to learn and reproduce cluster assignments on unseen data.

* **Cluster Evaluation:**  
  Evaluate the trained classifier using accuracy and classification metrics to ensure consistent cluster prediction.

---

## Data Source

Dataset sourced from Kaggle:  
[https://www.kaggle.com/datasets/uom190346a/e-commerce-customer-behavior-dataset](https://www.kaggle.com/datasets/uom190346a/e-commerce-customer-behavior-dataset)

The dataset was uploaded to a cloud-hosted database and ingested directly into the pipeline.

---

## Dataset Description

* Customer ID – Integer  
* Gender – Categorical  
* Age – Integer  
* City – Categorical  
* Membership Type – Categorical  
* Total Spend – Numeric  
* Items Purchased – Integer  
* Average Rating – Numeric  
* Discount Applied – Boolean  
* Days Since Last Purchase – Integer  
* Satisfaction Level – Categorical  

---

## Notes on Model Evaluation

This is a cluster segmentation project that uses labels as artificial labels, **cluster-generated labels** (pseudo-labels from KMeans) to train classification models.  
As a result, high classification accuracy reflects the model’s ability to **replicate cluster boundaries**, rather than predict a natural ground-truth label.

---

## Project Structure

The project is structured around modular data science pipelines implemented in the src/components and src/pipeline packages. Configuration is managed centrally via YAML files and configuration classes. Experiments and exploratory work are tracked in versioned notebooks. Persistent storage is handled through MongoDB using the persistence module, and a Streamlit UI enables real-time customer inference.


customer_segmentation/
│
├── config/
│   ├── config.yaml
│   ├── param.yaml
│   └── schema.yaml
│
├── notebooks/
│   ├── 01_exploratory_data_analysis.ipynb
│   ├── 02_clustering_experiments.ipynb
│   └── 03_cluster_profiling.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── data_clustering.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── persistence/
│   │   ├── database.py
│   │   └── historic_upsert.py
│   │
│   ├── utils/
│   │   ├── common.py
│   │   └── model_registry.py
│   │
│   ├── entity/
│   │   ├── config_entity.py
│   │   └── artifact_entity.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── configuration.py
│   │
│   ├── constants/
│   │   └── __init__.py
│   │
│   ├── logger.py
│   └── exception.py
│
├── artifact/
│   ├── data_ingestion/
│   │   └── customer_segmentation.csv
│   │
│   ├── data_transformation/
│   │   ├── transformed_data.npy
│   │   └── transformer.pkl
│   │
│   ├── data_clustering/
│   │   ├── train.npy
│   │   ├── test.npy
│   │   └── labels.csv
│   │
│   ├── model_trainer/
│   │   └── trained_model.pkl
│   │
│   └── model_evaluation/
│       └── metrics.txt
│
├── app.py
├── pages/
│   └── account_creation.py
│
├── requirements.txt
├── README.md
└── .env

---

## Training Pipeline and Upsert Demo

![Training Pipeline Demo](assets/training_pipeline_and_upsert.gif)

----
 
## Prediction Pipeline Demo

![Prediction Pipeline Demo](assets/prediction_pipeline.git)

---

## Future Work

* Use AWS Secrets Manager to securely store database credentials.
* Migrate data storage to AWS DynamoDB and S3 for scalable ingestion and model storage.
* Implement CI/CD using GitHub Actions, AWS Elastic Beanstalk, and AWS CodePipeline.
