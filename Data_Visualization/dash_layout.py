import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Add Dataframe
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]
})

# Add Bar Graph
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode='group')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        children='Dashboard',
        style={'text-align': 'center'}
    ),
    # Create Dropdown
    dcc.Dropdown(options=[
            {'label' : 'New York City', 'value' : 'NYC'},
            {'label' : 'Montreal', 'value' : 'MTL'},
            {'label' : 'San Francisco', 'value' : 'SF'}
        ],
        value='NYC'
    ),

    # Bar Graph
    dcc.Graph(id='example-graph-2', figure=fig)
])




if __name__ == '__main__':
    app.run_server(debug=True, port=5000, host='localhost')