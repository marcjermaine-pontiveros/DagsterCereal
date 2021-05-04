from modules.solids import download_cereals, find_sugariest
from dagster import pipeline

@pipeline
def serial_pipeline():
    find_sugariest(download_cereals())

