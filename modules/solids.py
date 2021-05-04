import pandas as pd 
from pandas_profiling import ProfileReport
import requests
import csv
from dagster import solid

'''
All Solids Definition
---------------------

'''


@solid
def hello_cereal(context):
    '''
    Single-Solid Pipeline
    ---------------------
    This solid downloads a csv of cereal data, reads it into a list of
    dictionaries which each represent a row in the CSV, and logs the 
    number of rows it finds.
    '''
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    context.log.info(f"Found {len(cereals)} cereals")
    return cereals

@solid
def download_cereals(_):
    '''
    Connecting Solids in Pipelines
    ------------------------------
    This solid downloads a csv of cereal data, reads it into a list of
    dictionaries which each represent a row in the CSV, and it returns 
    the list of dictionaries to be consumed by other solid.
    '''
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    return [row for row in csv.DictReader(lines)]


@solid
def find_sugariest(context, cereals):
    '''
    Connecting Solids in Pipelines
    ------------------------------
    This solid consumes the list of dictionaries from `download_cereals` solid.
    '''
    sorted_by_sugar = sorted(cereals, key=lambda cereal: cereal["sugars"])
    context.log.info(f'{sorted_by_sugar[-1]["name"]} is the sugariest cereal')


@solid
def find_highest_calorie_cereal(_, cereals):
    sorted_cereals = list(
        sorted(cereals, key=lambda cereal: cereal["calories"])
    )
    return sorted_cereals[-1]["name"]


@solid
def find_highest_protein_cereal(_, cereals):
    sorted_cereals = list(
        sorted(cereals, key=lambda cereal: cereal["protein"])
    )
    return sorted_cereals[-1]["name"]

@solid
def display_results(context, most_calories, most_protein):
    context.log.info(f"Most caloric cereal: {most_calories}")
    context.log.info(f"Most protein-rich cereal: {most_protein}")

@solid 
def profile_cereal(_):
    cereal_df = pd.read_csv("https://docs.dagster.io/assets/cereal.csv")
    profile = ProfileReport(cereal_df, title="Cereals Profiling Report")
    profile.to_file("output.html")
    _.log.info(f"Profiling test complete!")

