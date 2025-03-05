## Analysis of Customer behaviour and Segmentation(in  progress)

## Project Overview



### Project approach

Even though this dataset is static. However, for this project I am treating this project as if there is a continuous data flow into the database. 

### Project Objectives & Approach

* **Data Cleaning and Transformation:** Clean the dataset by handling missing values, duplicated values and outliers.
* **Feature Engineering:** Develop new features based on transactional data.
* **Data Preprocessing:** Undertake feature scaling and dimensionality reduction to streamline the data which will enhance clustering process.
* **Customer Segmentation using KMeans Clustering:** This is segmenting cudtomers into distinct groups using k-means. This will help in facilitating targeted marketing and personalized strategies.
* **Cluster Analysis & Evaluation:** Analyze and profile each customer to develop targeted marketing strategies and assess the quality of each cluster.

## Data Source

data source -[https://www.kaggle.com/datasets/ravalsmit/customer-segmentation-data?resource=download](https://www.kaggle.com/datasets/ravalsmit/customer-segmentation-data?resource=download)

I uploaded the data into a cloud database. 

### Dataset description:

* CUST_ID: Unique identifier for each customer.
* BALANCE: The outstanding balance to be paid in a credit card by the customer.
* BALANCE_FREQUENCY: Frequency of updating the balance on credit card.
* PURCHASES: Total amount of purchases made using the credit card.
* ONEOFF_PURCHASES: Total amount of one time purchase made using the credit card.
* INSTALLMENTS_PURCHASES: Total amount of purchases made using installment plan using credit card.
* CASH_ADVANCE: Total amount of cash advances taken from the credit card.
* PURCHASE_FREUENCY: Indicate how often purchases are made using credit card.
* ONEOFF_PURCHASES_FREQUENCY: Frequency of one time purchase.
* PURCHASES_INSTALLMENTS_FREQUENCY: Frequency of purchse using installment plans.
* CASH_ADVANCE_FREQUENCY: 
* CASH_ADVANCE_TRX: Number of transactions made for cash advances.
* PURCHASES_TRX: Number of purchase transactions made using the credit card.
* CREDIT_LIMIT: The credit limit assigned to the customer.
* PAYMENTS: Total amount of payments made by the customer.
* MINIMUM_PAYMENTS: Minimum amount due for payments.
* PRC_FULL_PAYMENT: Percentage of the full credit card bill paid by the customer.
* TENURE: Number of months the customer has been using the credit card.

## Future Works
* Use AWS Secret manager to store my database and connection information.
* Store my data in AWS dynamoDB and attach an S3 bucket for easy ingestion and also to store my models.
* Use github action with Elasticbeanstalk, codepipeline for continous deployment.