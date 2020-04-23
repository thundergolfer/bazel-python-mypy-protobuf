# bazel-python-mypy-protobuf
Repro thundergolfer/bazel-mypy-integration issue #15

### Usage

⚠️ _Note:_ `python` should point to Python3.

`bazel run //demo`

or

`USE_BAZEL_VERSION=2.x.0 bazelisk run //demo`

Works with bazel:

  - 2.0.0
  - 2.1.0
  - 2.2.0

and passes bazel-mypy-integration tests
