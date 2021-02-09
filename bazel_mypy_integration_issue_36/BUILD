load("@rules_python//python:defs.bzl", "py_runtime_pair")

py_runtime(
    name = "my_py3_runtime",
    interpreter_path = "/Users/jonathon/Code/thundergolfer/bazel-python-mypy-protobuf/bazel_mypy_integration_issue_36/.venv/bin/python",
    python_version = "PY3",
)

py_runtime_pair(
    name = "my_py_runtime_pair",
    py2_runtime = None,
    py3_runtime = ":my_py3_runtime",
)

toolchain(
    name = "python_toolchain",
    toolchain = ":my_py_runtime_pair",
    toolchain_type = "@rules_python//python:toolchain_type",
)