## Connecting Solids in Pipelines

Our pipelines wouldn't be very interesting if they were limited to single solids. Pipelines connect solids into arbitrary DAGs of computation.

Why split up code into solids instead of splitting it up into regular Python functions? There are a few reasons:

- Dagster can execute sets of solids without executing the entire pipeline. This means that, if we hit a failure in our pipeline, we can re-run just the steps that didn't complete successfully, which often allows us to avoid re-executing expensive steps.

- When two solids don't depend on each other, Dagster can execute them simultaneously.

- Dagster can materialize the output of a solid to persistent storage. IOManagers let us separate business logic from IO, which lets us write code that's more testable and portable across environments.

Dagster pipelines model a dataflow graph. In data pipelines, the reason that a later step comes after an earlier step is almost always that it uses data produced by the earlier step. Dagster models these dataflow dependencies with inputs and outputs.

## Let's Get Serial

We'll expand the pipeline we worked with in the first section of the tutorial into two solids:

- The first solid will download the cereal data and return it as an output.

- The second solid will consume the cereal data produced by the first solid and find the cereal with the most sugar. 

This will allow us to re-run the code that finds the sugariest cereal without re-running the code that downloads the cereal data. If we spot a bug in our sugariness code, or if we decide we want to compute some other statistics about the cereal data, we won't need to re-download the data.