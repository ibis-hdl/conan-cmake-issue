# [Using Host and Build Profile from CMakePresets #678](https://github.com/conan-io/cmake-conan/issues/678)

Using [CMake-Conan provider](https://github.com/conan-io/cmake-conan), where conan presets are:

```
> conan profile show -pr=default
Host profile:
[settings]
arch=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=gnu17
compiler.libcxx=libstdc++11
compiler.version=13
os=Linux

Build profile:
[settings]
arch=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=gnu17
compiler.libcxx=libstdc++11
compiler.version=13
os=Linux
```

```
> conan profile show -pr=clang-libc++
Host profile:
[settings]
arch=x86_64
build_type=Release
compiler=clang
compiler.cppstd=gnu17
compiler.libcxx=libc++
compiler.version=18
os=Linux
[conf]
tools.build:compiler_executables={'c': '/usr/bin/clang', 'cpp': '/usr/bin/clang++'}
[buildenv]
CC=clang
CXX=clang++

Build profile:
[settings]
arch=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=gnu17
compiler.libcxx=libstdc++11
compiler.version=13
os=Linux
```
Using simple Clang works as expected:
```
> rm -rf build; cmake --preset clang && cmake --build --preset clang-release
```

where with libc++ failed to compile due to conan's dependency:
```
> rm -rf build; cmake --preset clang-libc++ && cmake --build --preset clang-libc++-release
```
Simply run `python3 build.py` to face the issue. I create all the profiles by using *devcontainer* `postStartCommand.sh` `configure_conan_profile()`.
