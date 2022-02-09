import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

cereal = pd.read_csv(DATA_PATH.joinpath('cereal.csv'))

layout = html.Div([

html.Div([
        html.Div([


            html.P('Select manufacturer', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px'}),
            dcc.Dropdown(id = 'select_mfr1',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': True},
                         value = 'K',
                         placeholder = 'Select mfr',
                         options = [{'label': c, 'value': c}
                                    for c in (cereal['mfr'].unique())], className = 'dcc_compon'),

            ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px"}),

    ], className = "row flex-display"),

            html.Div([
                html.Div([

                    dcc.Graph(id = 'line_chart1',
                              config = {'displayModeBar': 'hover'}),

                ], className = "create_container2 six columns"),

            ], className = "row flex-display"),




], id="mainContainer", style={"display": "flex", "flex-direction": "column"})

@app.callback(Output('line_chart1', 'figure'),
              [Input('select_mfr1', 'value')])
def update_graph(select_mfr1):
    cereal1 = cereal.groupby(['name', 'mfr', 'type'])[['calories', 'protein', 'fat', 'sodium']].sum().reset_index()
    cereal2 = cereal1[cereal1['mfr'] == select_mfr1]



    return {
        'data':[go.Bar(
                    x=cereal2['name'],
                    y=cereal2['calories'],

                    name = 'calories',
                    marker = dict(color = '#FF00FF'
                          ),
                    hoverinfo='text',
                    hovertext=
                    '<b>name</b>: ' + cereal2['name'].astype(str) + '<br>' +
                    '<b>mfr</b>: ' + cereal2['mfr'] + '<br>' +
                    '<b>type</b>: ' + cereal2['type'].astype(str) + '<br>' +
                    '<b>calories</b>: ' + [f'{x:,.0f}' for x in cereal2['calories']] + '<br>'



              ),

            go.Bar(
                x = cereal2['name'],
                y = cereal2['sodium'],

                name = 'sodium',

                marker = dict(color = 'orange'
                              ),
                hoverinfo = 'text',
                hovertext =
                '<b>name</b>: ' + cereal2['name'].astype(str) + '<br>' +
                '<b>mfr</b>: ' + cereal2['mfr'] + '<br>' +
                '<b>type</b>: ' + cereal2['type'].astype(str) + '<br>' +
                '<b>sodium</b>: ' + [f'{x:,.0f}' for x in cereal2['sodium']] + '<br>'

            )],


        'layout': go.Layout(
             barmode = 'stack',
             plot_bgcolor='#F2F2F2',
             paper_bgcolor='#F2F2F2',
             title={
                'text': 'Comparison: Calories and Sodium',

                'y': 0.96,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
             titlefont={
                        'color': 'black',
                        'size': 15},
             margin = dict(b=170),
             hovermode='closest',
             xaxis=dict(title='<b></b>',
                        color='black',
                        showline=True,
                        showgrid=False,
                        linecolor='black',
                        linewidth=1,


                ),

             yaxis=dict(title='<b>calories and sodium</b>',
                        color='black',
                        showline=False,
                        showgrid=True,
                        linecolor='black',

                ),

            legend = {
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'x': 0.5,
                'y': 1.25,
                'xanchor': 'center',
                'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'black',


                 )
        )

    }
