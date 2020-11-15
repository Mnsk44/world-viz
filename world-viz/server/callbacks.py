from dash.dependencies import Input, Output
import dash_core_components as dcc
from data.relative_growth import fastest_relative_pop_growth
from data.gnp_life_expectancy import gnp_and_life_expectancy
from data.english_countries_and_city_populations import english_speaking_city_populations
from server.app import app

@app.callback(
    Output("tabs-content", "children"),
    [Input("tabs", "value")]
)
def get_tab_content(tab):
    fig = None
    if tab == "relative-growth":
        fig = fastest_relative_pop_growth()
    elif tab == "gnp":
        fig = gnp_and_life_expectancy()
    elif tab == "city":
        fig = english_speaking_city_populations()

    return dcc.Graph(
        id="relative-growth-fig",
        figure=fig
    )
