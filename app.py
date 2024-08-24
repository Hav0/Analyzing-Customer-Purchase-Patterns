from cleaning import *
from dash import Dash, dcc, html, Input, Output
import plotly.express as px 

# bar chart for product categories and purchase frequency

bar_plot = px.bar(customer_data, x = 'preferred_category', y = 'number of purchases (1 year)', color = 'gender',
                              title = "Purchase Frequencies based on Product Category and Gender")

# box plot for income distribution and gender
 
box_plot = px.box(customer_data, x = 'gender', y = 'income', 
                  title = 'Distribution of Income Based on Gender',
                  category_orders={'gender': ['Male', 'Female', 'Other']})


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
app.title = 'Understanding Customer Purchase Patterns'

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
        dcc.Graph(figure = bar_plot, config={"displayModeBar": False}, className = 'bar-plot',),
        html.Div(
            children = [html.P(children = 'Move the slider to modify the minimum or maximum value of the boxplot below:', className = 'slider-description')]
        ),
        dcc.RangeSlider(id = 'income-slider', min=customer_data['income'].min(), max = customer_data['income'].max(),
                        value=[customer_data['income'].min(), customer_data['income'].max()], className = 'income-slider'),
        dcc.Graph(id = 'box-plot', figure = box_plot, config={"displayModeBar": False}, className = 'box-plot',),
       
    ]
)

# define callbacks to implement interactivity 
@app.callback(
    Output('box-plot', 'figure'),
    Input('income-slider', 'value')
)
def update_box_plot(inc_value):
    new_data = customer_data.query('income >= @inc_value[0] and income <= @inc_value[1]')
    updated_box_plot = px.box(new_data, x='gender', y='income', 
                             title='Distribution of Income Based on Gender',
                             category_orders={'gender': ['Male', 'Female', 'Other']})
    return updated_box_plot

if __name__ == "__main__":
    app.run_server(debug=True, port = 8051)
