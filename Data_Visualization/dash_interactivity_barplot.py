import pandas as pd
import plotly.express as px
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
    html.H1('Total number of flights to the destination state split by reporting air', 
            style={'text-align': 'center', 'color': '#503D36', 'font-size': 50}),

    html.Div(['Input Year: ', dcc.Input(id='input-year', value='2010', type='number',
                                        style={'height': '50px', 'font-size': 35})],
                                        style={'font-size': 40}),
    
    html.Br(),
    html.Br(),

    html.Div(dcc.Graph(id='bar-plot')),
], style={'font-size': 35})


# add callback decorator
@app.callback(Output(component_id='bar-plot', component_property='figure'), 
              Input(component_id='input-year', component_property='value'))

def get_graph(entered_year):
    # select data based on year
    df = airline_data[airline_data['Year'] == int(entered_year)]
    # group the data by deststate
    bar_data = df.groupby(by='DestState')['Flights'].sum().reset_index()
    fig = px.bar(bar_data, x='DestState', y='Flights', title='Flights to Destination State')

    

    return fig


# Run app
if __name__ == '__main__':
    app.run_server(port=5000, host='localhost', debug=True)