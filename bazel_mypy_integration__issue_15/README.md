# bazel-python-mypy-protobuf
Repro thundergolfer/bazel-mypy-integration issue #15

### Usage

⚠️ _Note:_ `python` should point to Python3.

`bazel run //demo`


Error I get:

```
ERROR: /Users/jonathonbelotti/Code/thundergolfer/bazel-python-mypy-protobuf/demo/BUILD.bazel:1:1: MyPy demo/demo_dummy_out failed (Exit 1): demo_mypy_exe failed: error executing command
  (cd /private/var/tmp/_bazel_jonathonbelotti/8138ded22aa26d087c58867ec9acc6a6/sandbox/darwin-sandbox/178/execroot/bazel_python_mypy_protobuf && \
  exec env - \
    PATH=/Users/jonathonbelotti/.cabal/bin:/Users/jonathonbelotti/.ghcup/bin:/usr/local/opt/scala@2.11/bin:/usr/local/opt/ruby/bin:/Users/jonathonbelotti/.pyenv/shims:/Users/jonathonbelotti/.local/bin:/usr/local/bin:/Users/jonathonbelotti/bin:/usr/local/bin:/Applications/Postgres.app/Contents/Versions/latest/bin:/Users/jonathonbelotti/Downloads/apache-maven-3.5.3/bin:/Users/jonathonbelotti/Downloads/google-cloud-sdk/bin:/Users/jonathonbelotti/.nix-profile/bin:/Users/jonathonbelotti/.nimble/bin:/Users/jonathonbelotti/.cargo/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin:/opt/X11/bin:/Users/jonathonbelotti/go/bin:/usr/local/Cellar/node/9.8.0/bin/ \
  bazel-out/darwin-fastbuild/bin/demo/demo_mypy_exe)
Execution platform: @local_config_platform//:host

Use --sandbox_debug to see verbose messages from the sandbox demo_mypy_exe failed: error executing command
  (cd /private/var/tmp/_bazel_jonathonbelotti/8138ded22aa26d087c58867ec9acc6a6/sandbox/darwin-sandbox/178/execroot/bazel_python_mypy_protobuf && \
  exec env - \
    PATH=/Users/jonathonbelotti/.cabal/bin:/Users/jonathonbelotti/.ghcup/bin:/usr/local/opt/scala@2.11/bin:/usr/local/opt/ruby/bin:/Users/jonathonbelotti/.pyenv/shims:/Users/jonathonbelotti/.local/bin:/usr/local/bin:/Users/jonathonbelotti/bin:/usr/local/bin:/Applications/Postgres.app/Contents/Versions/latest/bin:/Users/jonathonbelotti/Downloads/apache-maven-3.5.3/bin:/Users/jonathonbelotti/Downloads/google-cloud-sdk/bin:/Users/jonathonbelotti/.nix-profile/bin:/Users/jonathonbelotti/.nimble/bin:/Users/jonathonbelotti/.cargo/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin:/opt/X11/bin:/Users/jonathonbelotti/go/bin:/usr/local/Cellar/node/9.8.0/bin/ \
  bazel-out/darwin-fastbuild/bin/demo/demo_mypy_exe)
Execution platform: @local_config_platform//:host

Use --sandbox_debug to see verbose messages from the sandbox
darwin-fastbuild is not a valid Python package name
Aspect @mypy_integration//:mypy.bzl%mypy_aspect of //demo:demo failed to build
INFO: Elapsed time: 90.811s, Critical Path: 20.08s
INFO: 177 processes: 177 darwin-sandbox.
FAILED: Build did NOT complete successfully
FAILED: Build did NOT complete successfully
```
