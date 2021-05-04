# A Single-Solid Pipeline

## Solids and Pipelines

Dagster's core abstractions are [solids](https://docs.dagster.io/concepts/solids-pipelines/solids) and [pipelines](https://docs.dagster.io/concepts/solids-pipelines/pipelines). By default, all solids in a pipeline execute in the same process. In production environments, Dagster is usually configured so that each solid executes in its own process.

In this section, we'll cover how to define a simple pipeline with a single solid, and then execute it.

## The Cereal Dataset

Our pipeline will operate on a simple but scary CSV dataset, cereal.csv, which contains nutritional facts about 80 breakfast cereals.

## Hello, Solid

Let's write our first Dagster solid and save it as `hello_cereal.py`.

A `solid` is a unit of computation in a data pipeline. Typically, you'll define solids by annotating ordinary Python functions with the `@solid` decorator.

Our first solid does three things: downloads a csv of cereal data, reads it into a list of dictionaries which each represent a row in the CSV, and logs the number of rows it finds.

```python
import requests
import csv
from dagster import pipeline, solid


@solid
def hello_cereal(context):
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    context.log.info(f"Found {len(cereals)} cereals")
```

## Hello, Pipeline

To execute our solid, we'll embed it in an equally simple `pipeline`. A `pipeline` is a set of solids arranged into a DAG of computation. You'll typically define pipelines by annotating ordinary Python functions with the `@pipeline` decorator.

```python
@pipeline
def hello_cereal_pipeline():
    hello_cereal()
```

Here you'll see that we call `hello_cereal()`. This call doesn't actually execute the solid. Within the bodies of functions decorated with `@pipeline`, we use *function calls* to indicate the dependency structure of the solids making up the pipeline. Here, we indicate that the execution of `hello_cereal` doesn't depend on any other solids by calling it with no arguments.


## Executing Our First Pipeline 
Assuming you’ve saved this pipeline as `hello_cereal.py`, you can execute it via any of three different mechanisms:

### Dagit 
To visualize your pipeline (which only has one node) in Dagit, from the directory in which you've saved the pipeline file, just run:

```
dagit -f hello_cereal.py
```

## Dagster CLI
From the directory in which you've saved the pipeline file, just run:

```
dagster pipeline execute -f hello_cereal.py
```

You'll see the full stream of events emitted by Dagster appear in the console, including our call to the logging machinery, which will look like:

```
2021-02-05 08:50:25 - dagster - INFO - system - ce5d4576-2569-44ff-a14a-51010eea5329 - hello_cereal - Found 77 cereals
```

## Python API

If you'd rather execute your pipelines as a script, you can do that without using the Dagster CLI at all. Just add a few lines to `hello_cereal.py`.

```python
## hello_cereal.py
from dagster import execute_pipeline

if __name__ == "__main__":
    result = execute_pipeline(hello_cereal_pipeline)
```

Now you can just run:
```
python hello_cereal.py
```

The `execute_pipeline()` function called here is the core Python API for executing Dagster pipelines from code.