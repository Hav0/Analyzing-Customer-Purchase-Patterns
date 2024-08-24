from cleaning import *
from dash import Dash, dcc, html
import plotly.express as px 

# bar chart for product categories and purchase frequency

bar_plot = px.bar(customer_data, x = 'preferred_category', y = 'number of purchases (1 year)', color = 'gender',
                              title = "Purchase Frequencies based on Product Category and Gender")

# box plot for income distribution and gender

box_plot = px.box(customer_data, x = 'gender', y = 'income(thousands of dollars)', 
                  title = 'Distribution of Income Based on Gender')

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Poppins:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    }
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Customer Segmentation Analytics: How Can We Learn More About Customer Purchase Data?'

# Create the app layout
app.layout = html.Div(
    children=[
        html.Div(
            children = [
            html.H1(children="Customer Analytics Based on Demographic Segmentation", className= 'header-title'),
            html.P(children="Analyzing customer purchase data based on their age, gender, and income as well as which categories of products customers of various demographics prefer."
            ,className = 'description'), 
            ],
            className = 'header'
        ),
        dcc.Graph(figure = bar_plot, config={"displayModeBar": False}, className = 'bar-plot'),
        dcc.Graph(figure = box_plot, config={"displayModeBar": False}, className = 'box-plot'),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port = 8051)
