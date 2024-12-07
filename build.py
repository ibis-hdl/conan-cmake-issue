import os, shutil, subprocess

def run(cmd):
    os.system(cmd)

try:
    shutil.rmtree("build")
except:
    pass

run("conan version")

"""
$ conan profile show -pr=clang
Host profile:
[settings]
arch=x86_64
build_type=Release
compiler=clang
compiler.cppstd=gnu17
compiler.libcxx=libstdc++11
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
"""

run("conan install . --settings build_type=Release --conf tools.cmake.cmaketoolchain:generator='Ninja Multi-Config' --build=missing --profile:all=clang")
run('cmake --preset clang')
run('cmake --build --preset clang-release')

"""
$ conan profile show -pr=clang-libc++
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
"""

run("conan install . --settings build_type=Release --conf tools.cmake.cmaketoolchain:generator='Ninja Multi-Config' --build=missing --profile:all=clang-libc++")
run('cmake --preset clang-libc++')
run('cmake --build --preset clang-libc++release')

run("cmake --list-presets")
