import dash
from dash import dcc

from dash import html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Create a Dash app
app = dash.Dash(__name__)

# Prepare the data with regions (make sure your actual dataset contains this)
data = {
    'date': ['2020-12-01', '2020-12-02', '2020-12-03', '2021-01-14', '2021-01-15', '2021-01-16'],
    'sales_value': [200, 210, 230, 250, 300, 320],
    'region': ['north', 'east', 'south', 'west', 'north', 'east']  # Example regions
}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create a function to update the chart based on the selected region
def filter_data(region):
    if region == 'all':
        return df
    return df[df['region'] == region]

# App layout
app.layout = html.Div(children=[
    html.H1('Sales Visualizer for Soul Foods', style={'textAlign': 'center'}),
    
    # Add radio button for region selection
    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All Regions', 'value': 'all'}
        ],
        value='all',  # Default value
        labelStyle={'display': 'inline-block', 'margin': '0 10px'},
        style={'textAlign': 'center'}
    ),
    
    # Line chart will be dynamically updated
    dcc.Graph(id='sales-line-chart')
])

# Callback to update the chart based on region selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(region):
    filtered_df = filter_data(region)
    fig = px.line(filtered_df, x='date', y='sales_value', title=f'Sales Over Time ({region.capitalize()} Region)' if region != 'all' else 'Sales Over Time')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
