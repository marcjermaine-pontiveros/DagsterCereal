from modules.solids import hello_cereal
from dagster import pipeline

'''
Example Pipeline
----------------
Uses solids defined modules.solids
'''

@pipeline
def hello_cereal_pipeline():
    hello_cereal()