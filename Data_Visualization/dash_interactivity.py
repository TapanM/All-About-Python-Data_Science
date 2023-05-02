import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


airline_data =  pd.read_csv('./airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Airline Performance Dashboard', 
            style={'text-align': 'center', 'color': '#503D36', 'font-size': 40}),

    html.Div(['Input Year: ', dcc.Input(id='input-year', value='2010', type='number',
                                        style={'height': '50px', 'font-size': 35})],
                                        style={'font-size': 40}),
    
    html.Br(),
    html.Br(),

    html.Div(dcc.Graph(id='line-plot'))
])


# add callback decorator
@app.callback(Output(component_id='line-plot', component_property='figure'), 
              Input(component_id='input-year', component_property='value'))

def get_graph(entered_year):
    # select data based on year
    df = airline_data[airline_data['Year'] == int(entered_year)]

    # group the data by month
    line_data = df.groupby(by='Month')['ArrDelay'].mean().reset_index()

    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
    fig.update_layout(xaxis_title='Month', yaxis_title='ArrDelay', title='Month vs Average Delay Flight Time')

    return fig


# Run app
if __name__ == '__main__':
    app.run_server(port=5000, host='localhost', debug=True)