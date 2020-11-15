"""
Interface for fetching fastest relative growth of population
"""
import pandas as pd
import plotly.express as px
from dbconn.connect import DBConnection

DB = DBConnection()

def english_speaking_city_populations(count=20) -> pd.DataFrame:
    sql_query = '''SELECT city.name, city.population, c.name, c.population
                   FROM city
                   INNER JOIN country_language cl
                           ON city.country_code = cl.country_code
                   INNER JOIN country c
                           ON city.country_code = c.code
                   WHERE cl.language = 'English';
                '''
    data = DB.query(sql_query)
    data = pd.DataFrame.from_records(data,
                                     columns=["name",
                                              "city_population",
                                              "country",
                                              "country_population"])
    return _create_visualization(data.nlargest(count, "city_population"))

def _create_visualization(data):
    return px.bar(data,
                  x="name",
                  y="city_population",
                  title="Largest English speaking cities",
                  labels={
                      "city_population": "Population",
                      "name": "City",
                      "country_total": "Total in Country"
                  },
                  hover_data=["name",
                              "city_population",
                              "country",
                              "country_population"],
                  color="country"
                  ).update_xaxes(categoryorder="total ascending")