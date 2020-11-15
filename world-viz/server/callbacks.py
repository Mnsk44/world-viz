"""
Callbacks for dash app
"""

from dash.dependencies import Input, Output, State
import dash_core_components as dcc
from data.relative_growth import fastest_relative_pop_growth
from data.gnp_life_expectancy import gnp_and_life_expectancy
from data.english_countries_and_city_populations import english_speaking_city_populations
from data.country_population_growth import country_population_growth
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

    return [dcc.Graph(
        id="fig",
        figure=fig
    )]

@app.callback(
    Output("info", "children"),
    [Input("fig", "clickData")],
    [State("tabs", "value")]
)
def add_sub_content(click, tab):
    # Changing tab reset clickData so this callback will be fired also then.
    if tab =="relative-growth":
        # NOTE: Click object can be none, e.g. on startup, but atm if check
        # breaks the div completely so omitted for now
        country = click["points"][0]["label"]
        fig = country_population_growth(country)
        return [dcc.Graph(
            id="sub-fig",
            figure=fig
        )]
    else:
        return None
