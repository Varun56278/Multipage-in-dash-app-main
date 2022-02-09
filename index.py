import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import protein_fat, calories_sodium

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.Div([
        html.Div([
            html.Div([
                html.H3('Cereal Products', style = {'margin-bottom': '0px', 'color': 'black'}),
            ])
        ], className = "create_container1 four columns", id = "title"),

    ], id = "header", className = "row flex-display", style = {"margin-bottom": "25px"}),

    html.Div([
      html.Div([
        dcc.Link('Protein and Fat', href='/apps/protein_fat', style = {"margin-bottom": "20px", 'padding': '25px', 'fontWeight': 'bold', 'color': 'blue'}),
        dcc.Link('Calories and Sodium', href='/apps/calories_sodium', style = {"margin-bottom": "20px", 'padding': '25px', 'fontWeight': 'bold', 'color': 'blue'}),

        ], className = "create_container3 four columns", id = "title1"),

    ], id = "header1", className = "row flex-display"),

    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/protein_fat':
        return protein_fat.layout
    if pathname == '/apps/calories_sodium':
        return calories_sodium.layout
    else:
        return "Page Error! Please select a link"


if __name__ == '__main__':
    app.run_server(debug=False)