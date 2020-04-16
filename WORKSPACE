workspace(name = "bazel_python_mypy_protobuf")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

rules_python_version = "38f86fb55b698c51e8510c807489c9f4e047480e"

http_archive(
    name = "rules_python",
    sha256 = "c911dc70f62f507f3a361cbc21d6e0d502b91254382255309bc60b7a0f48de28",
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

# git repo for quick iterations
git_repository(
    name = "mypy_integration",
    commit = "943a34f635ff99629f49e3eda1b8ff70fa831b55",
    shallow_since = "1586997547 -0400",
    remote = "https://github.com/cemel-jhu/bazel-mypy-integration",
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

# Protobuf Support

http_archive(
    name = "build_stack_rules_proto",
    urls = ["https://github.com/stackb/rules_proto/archive/b93b544f851fdcd3fc5c3d47aee3b7ca158a8841.tar.gz"],
    sha256 = "c62f0b442e82a6152fcd5b1c0b7c4028233a9e314078952b6b04253421d56d61",
    strip_prefix = "rules_proto-b93b544f851fdcd3fc5c3d47aee3b7ca158a8841",
)

load("@build_stack_rules_proto//python:deps.bzl", "python_proto_library")

python_proto_library()

load("@rules_python//python:pip.bzl", "pip_repositories")
load("@rules_python//python:pip.bzl", "pip3_import")

pip_repositories()
pip3_import(
    name = "protobuf_py_deps",
    requirements = "@build_stack_rules_proto//python/requirements:protobuf.txt",
)

load("@protobuf_py_deps//:requirements.bzl", protobuf_pip_install = "pip_install")

protobuf_pip_install()
