"""
Database population script from data source
"""
import logging
import os
import sys
import pandas as pd
import pycountry
from dbconn.connect import DBConnection

LOGGER = logging.getLogger(__name__)

DATA_PATH = os.getenv("DATA_LOCATION", "data/world_population_1960_2015.csv")
DATA_ENCODING = os.getenv("DATA_ENCODING", "cp1252")
COUNTRIES = [country.name for country in pycountry.countries]
TARGET_TABLE = "population"

LOGGER.info("Starting to populate database...")
LOGGER.info("Loading data...")
data = pd.read_csv(DATA_PATH, encoding=DATA_ENCODING)
data = data[data['Country Name'].isin(COUNTRIES)]

try:
    LOGGER.info(f"Inserting data into database table: {TARGET_TABLE}")
    data.to_sql(TARGET_TABLE,
                DBConnection().engine,
                if_exists="fail",
                index=False)
    LOGGER.info("Database populated successfully!")
except ValueError as err:
    LOGGER.warning("Database table already exists", exc_info=err)
    sys.exit(0)

LOGGER.info("Database population finished, shutting down...")
