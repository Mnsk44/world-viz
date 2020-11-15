import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([
    html.H1("Hello World!"),
    html.Div([
        dcc.Tabs(id="tabs", value="relative-growth", children=[
            dcc.Tab(label="Relative Population Growth", value="relative-growth"),
            dcc.Tab(label="GNP and life expectancy", value="gnp")
        ]),
        html.Div(id="tabs-content")

    ])
])