# VLM Value Extraction

A custom Arkindex worker that pre-annotates elements by extracting values from an image and its keys. Extraction is made by an API call to an Ollama

## Development

For development and tests purpose it may be useful to install the worker as a editable package with pip.

```shell
pip install -e .
```

## Linter

Code syntax is analyzed before submitting the code.\
To run the linter tools suite you may use pre-commit.

```shell
pip install pre-commit
pre-commit run -a
```

## Run tests

Tests are executed with tox using [pytest](https://pytest.org).

```shell
pip install tox
tox
```

To recreate tox virtual environment (e.g. a dependencies update), you may run `tox -r`
