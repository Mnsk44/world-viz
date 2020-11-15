import dash_html_components as html
import dash_core_components as dcc
from dash_html_components.P import P

layout = html.Div([
    html.H1("World population infographics"),
    html.Div([
        dcc.Tabs(id="tabs", value="relative-growth", children=[
            dcc.Tab(label="Relative Population Growth", value="relative-growth"),
            dcc.Tab(label="GNP and life expectancy", value="gnp"),
            dcc.Tab(label="Largest English Speaking Cities", value="city")
        ])
    ]),
    html.Div(id="tabs-content"),
    html.Div(id="info")
])