import os, shutil, subprocess

def run(cmd):
    os.system(cmd)

try:
    shutil.rmtree("build")
except:
    pass

run("conan version")
run('cmake --preset clang')
run('cmake --build --preset clang-release')
run('cmake --preset clang-libc++')
run('cmake --build --preset clang-libc++release')
run("cmake --list-presets")
