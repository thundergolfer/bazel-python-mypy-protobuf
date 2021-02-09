## Setup

`python3 -m venv .venv`

### Install requirements

```sh
pip install protobuf mypy-protobuf
```

### Generate protobuf and stub file

```.sh
protoc --python_out=. ./proto/bling_api.proto --mypy_out=.
```

## Reproduce:

```
bazel test //... --test_output=all
```