load(
    "@build_stack_rules_proto//python:python_proto_library.bzl",
    "python_proto_library",
)

proto_library(
    name="person_proto",
    srcs=[
        "person.proto",
    ],
)

python_proto_library(
    name="core_python_proto",
    deps=[":person_proto"],
    visibility=[
        "//visibility:public"
    ]
)
