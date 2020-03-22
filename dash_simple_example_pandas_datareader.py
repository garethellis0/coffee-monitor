import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas import *
from datetime import datetime as dt

app = dash.Dash('Hello World')

app.layout = html.Div([
    html.H1("How Much Coffee Is Left?"),
    #dcc.Dropdown(
    #    id='my-dropdown',
    #    options=[
    #        {'label': 'Coke', 'value': 'COKE'},
    #        {'label': 'Tesla', 'value': 'TSLA'},
    #        {'label': 'Apple', 'value': 'AAPL'}
    #    ],
    #    value='COKE'
    #),
    dcc.Dropdown(id='dropdown'),
    dcc.Graph(
        id='my-graph',
        #figure={
        #    'data': [{
        #        'x': pandas.read_csv("data.csv")["time"],
        #        'y': pandas.read_csv("data.csv")["weight_grams"],
        #        }],
        #    'layout': {
        #        'title': 'Dash Data Visualization'
        #    }
        #}
    )], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'),  [Input('dropdown', 'value')])
def update_graph(dropdown_value):
    df = pandas.read_csv("data.csv")
    #df = web.DataReader(
    #    selected_dropdown_value,
    #    'google',
    #    dt(2017, 1, 1),
    #    dt.now()
    #)
    return {
        'data': [{
            'x': df["time"],
            'y': df["weight_grams"],
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(port=80, host='0.0.0.0')
