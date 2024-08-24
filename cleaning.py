import pandas as pd

customer_data = pd.read_csv("customer_segmentation_data.csv")
customer_data_null = pd.isnull(customer_data)
customer_data.dropna()

customer_data = customer_data.drop(['spending_score'], axis = 1)
#print(customer_data)

