load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")
load("@deps//:requirements.bzl", "requirement")
load("@mypy_integration//:rules.bzl", "mypy_stubs")
load("@mypy_integration//:mypy.bzl", "mypy_test")


mypy_stubs(
    name = "stubs",
    srcs = glob(["proto/*.pyi"])

)

py_library(
    name = "foo",
    srcs = glob(["*.py"]),
    srcs_version="PY3",
    deps = [
        ":stubs",
        requirement("protobuf"),
    ],
)

mypy_test(
    name="mypy_test_foo",
    deps=[
        ":foo",
        ":stubs"
    ]
)