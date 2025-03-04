import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Create a Dash app
app = dash.Dash(__name__)

# Prepare the data (use your own dataset here)
data = {
    'date': ['2020-12-01', '2020-12-02', '2020-12-03', '2021-01-14', '2021-01-15', '2021-01-16'],
    'sales_value': [200, 210, 230, 250, 300, 320]
}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create a line chart using Plotly Express
fig = px.line(df, x='date', y='sales_value', title='Sales Over Time')

# App layout
app.layout = html.Div(children=[
    html.H1('Sales Visualizer for Soul Foods', style={'textAlign': 'center'}),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
