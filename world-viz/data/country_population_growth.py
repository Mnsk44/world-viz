"""
Interface for fetching country specific population increase between 2000-2015
"""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dbconn.connect import DBConnection

DB = DBConnection()

def country_population_growth(country: str=None) -> go.Figure:
    years = [str(year) for year in range(2000,2016)]
    sql_query = '''SELECT "Country Name", "2000", "2001", "2002", "2003", "2004",
                          "2005", "2006", "2007", "2008", "2009", "2010", "2011",
                          "2012", "2013", "2014", "2015"
                   FROM population;
                '''
    data = DB.query(sql_query)
    data = pd.DataFrame.from_records(data,
                                     columns=["Country Name", *years])
    data = pd.melt(data,
                   id_vars=["Country Name"],
                   var_name="year",
                   value_name="population")
    if country:
        return _create_visualization(data[data["Country Name"] == country])

def _create_visualization(data: pd.DataFrame) -> go.Figure:
    return px.scatter(data,
                      x="year",
                      y="population",
                      title=f"{data['Country Name'].values[0]} population",
                      labels={
                          "year": "Year",
                          "population": "Population",
                          "Country Name": "Country"
                     }).update_layout(showlegend=False
                      ).update_traces(mode='lines+markers')