"""
Interface for fetching fastest relative growth of population
"""
import pandas as pd
import plotly.express as px
from dbconn.connect import DBConnection

DB = DBConnection()

def gnp_and_life_expectancy():
    sql_query = 'SELECT "name", "population", "life_expectancy", "gnp" FROM country;'
    data = DB.query(sql_query)
    data = pd.DataFrame.from_records(data,
                                     columns=["name",
                                              "population",
                                              "life_expectancy",
                                              "gnp"])
    data = data[data["population"] != 0]
    data["gnp_per_capita"] = (data["gnp"]*(10**6)) / data["population"]
    return _create_visualization(data[["name", "gnp_per_capita", "life_expectancy"]])


def _create_visualization(data):
    return px.scatter(data,
                  x="life_expectancy",
                  y="gnp_per_capita",
                  title="GNP per capita in relation to life expectancy",
                  labels={
                      "life_expectancy": "Life Expectancy",
                      "gnp_per_capita": "GNP per capita ($)",
                      "name": "Country"
                  },
                  hover_data=["name"]
                  ).update_layout(showlegend=False)