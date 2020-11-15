"""
Interface for fetching fastest relative growth of population
"""
import pandas as pd
import plotly.express as px
from dbconn.connect import DBConnection

DB = DBConnection()

def fastest_relative_pop_growth(count: int=10) -> pd.DataFrame:
    sql_query = 'SELECT "Country Name", "2000", "2015" FROM population;'
    data = DB.query(sql_query)
    data = pd.DataFrame.from_records(data,
                                     columns=["Country Name", "2000", "2015"])
    data = data.set_index("Country Name")
    data = data.pct_change(axis="columns").nlargest(count, "2015")["2015"]
    return _create_visualization(data.reset_index())

def _create_visualization(data):
    return px.bar(data,
                  x="Country Name",
                  y="2015",
                  title="Fastest relative population growth between 2000-2015",
                  labels={
                      "2015": "Relative Growth",
                      "Country Name": "Country"
                  }).update_layout(showlegend=False,
                                  yaxis_tickformat="%")