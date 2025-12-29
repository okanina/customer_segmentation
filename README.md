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

---

## Training Pipeline and Upsert Demo

![Training Pipeline Demo](assets/training_pipeline_and_upsert.gif)

----
 
## Prediction Pipeline Demo

![Prediction Pipeline Demo](https://github.com/okanina/customer_segmentation/blob/main/assets/prediction_pipeline.gif)

---

## Future Work

* Use AWS Secrets Manager to securely store database credentials.
* Migrate data storage to AWS DynamoDB and S3 for scalable ingestion and model storage.
* Implement CI/CD using GitHub Actions, AWS Elastic Beanstalk, and AWS CodePipeline.
