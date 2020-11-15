from dash.dependencies import Input, Output
import dash_core_components as dcc
from data.relative_growth import fastest_relative_pop_growth
from server.app import app

@app.callback(
    Output("tabs-content", "children"),
    [Input("tabs", "value")]
)
def get_tab_content(tab):
    fig = None
    if tab == "relative-growth":
        fig = fastest_relative_pop_growth()

    return dcc.Graph(
        id="relative-growth-fig",
        figure=fig
    )
