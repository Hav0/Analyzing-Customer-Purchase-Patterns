import pandas as pd

customer_data = pd.read_csv("customer_segmentation_data.csv")
customer_data_null = pd.isnull(customer_data)
customer_data.dropna()

customer_data = customer_data.drop(['spending_score'], axis = 1)
customer_data = customer_data.rename(columns = {'income':'income(thousands of dollars)', 'purchase_frequency': 'number of purchases (1 year)'})
#print(customer_data)

