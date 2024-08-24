from cleaning import *
from dash import Dash, dcc, html
import plotly.express as px 

# bar chart for product categories and purchase frequency

bar_plot = px.bar(customer_data, x = 'preferred_category', y = 'purchase_frequency', color = 'gender',
                              title = "Purchase Frequencies based on Product Category and Gender")

# box plot for income distribution and gender

box_plot = px.box(customer_data, x = 'gender', y = 'income', 
                  title = 'Distribution of Income Based on Gender')

app = Dash(__name__)

# Create the app layout
app.layout = html.Div(
    children=[
        html.H1(children="Customer Segmentation Analytics"),
        html.P(children="Analyze customer purchase data based on age, gender, and income as well as which categories of products customers of various demographics prefer."),
        dcc.Graph(figure = bar_plot), 
        dcc.Graph(figure = box_plot),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port = 8051)
