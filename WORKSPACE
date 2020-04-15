workspace(name="bazel_python_mypy_protobuf")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

rules_python_version = "7b222cfdb4e59b9fd2a609e1fbb233e94fdcde7c"

http_archive(
    name = "rules_python",
    sha256 = "d2865e2ce23ee217aaa408ddaa024ca472114a6f250b46159d27de05530c75e3",
    strip_prefix = "rules_python-{version}".format(version = rules_python_version),
    url = "https://github.com/bazelbuild/rules_python/archive/{version}.tar.gz".format(version = rules_python_version),
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

# dillon-giacoppo/rules_python_external

rules_python_external_version = "0.1.4"

http_archive(
    name = "rules_python_external",
    sha256 = "c3f3fae1bd624b83dcc6e83cd8e7e6e574189c7ed4f56f51dd0be9c50354cc9e",
    strip_prefix = "rules_python_external-{version}".format(version = rules_python_external_version),
    url = "https://github.com/dillon-giacoppo/rules_python_external/archive/v{version}.zip".format(version = rules_python_external_version),
)

load("@rules_python_external//:repositories.bzl", "rules_python_external_dependencies")

rules_python_external_dependencies()

load("@rules_python_external//:defs.bzl", "pip_repository")

pip_repository(
    name = "pypi",
    requirements = "//third_party:requirements.txt",
)

# MyPy

mypy_integration_version = "0.0.7"

http_archive(
    name = "mypy_integration",
    sha256 = "bf7ecd386740328f96c343dca095a63b93df7f86f8d3e1e2e6ff46e400880077",
    strip_prefix = "bazel-mypy-integration-{version}".format(version = mypy_integration_version),
    url = "https://github.com/thundergolfer/bazel-mypy-integration/archive/{version}.zip".format(
        version = mypy_integration_version,
    ),
)

load(
    "@mypy_integration//repositories:repositories.bzl",
    mypy_integration_repositories = "repositories",
)

mypy_integration_repositories()

load("@mypy_integration//:config.bzl", "mypy_configuration")

mypy_configuration("//tools/python/typing:mypy.ini")

load("@mypy_integration//repositories:deps.bzl", mypy_integration_deps = "deps")

mypy_integration_deps("//tools/python/typing:mypy_version.txt")

load("@mypy_integration//repositories:pip_repositories.bzl", mypy_integration_pip_deps = "pip_deps")

mypy_integration_pip_deps()
