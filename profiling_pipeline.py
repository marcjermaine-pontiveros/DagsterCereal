from modules.solids import profile_cereal
from dagster import pipeline

@pipeline
def cereals_df_profiling_pipeline():
    profile_cereal()