from modules.solids import download_cereals, find_highest_calorie_cereal, find_highest_protein_cereal, display_results
from dagster import pipeline

@pipeline
def complex_pipeline():
    cereals = download_cereals()
    display_results(
        most_calories=find_highest_calorie_cereal(cereals),
        most_protein=find_highest_protein_cereal(cereals),
    )