# Setup for the Tutorial 
Welcome to the Dagster tutorial! Before we get started, we need to install Dagster on our machine.

## Python and pip 
We’ll assume that you have some familiarity with Python, but you should be able to follow along even if you’re coming from a different programming language. To check that Python and the pip package manager are already installed in your environment or install them, you can follow the instructions here.

## Dagster and Dagit 
If you haven't already, please read about our Installation page.

```
pip install dagster dagit requests
```

This installs a few modules:

- Dagster: the core programming model and abstraction stack; stateless, single-node, single-process and multi-process execution engines; and a CLI tool for driving those engines.

- Dagit: the UI for developing and operating Dagster pipelines, including a DAG browser, a type-aware config editor, and a live execution interface.

- Requests: not part of Dagster. Our examples will use it to download data from the internet.

You can also follow the Quick Start section to make sure you have installed the packages and set up the environment properly.

[A Single-Solid Pipeline](SingleSolid.md)

[Connecting Solids in Pipelines](ConnectingSolid.md)