# [Recipe tools](https://docs.conan.io/2/reference/tools.html)
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import load, save
import json
import os

class ActionTestRecipe(ConanFile):
    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("catch2/3.7.1")

    def layout(self):
        # see: conan.io #17324
        #self.folders.build_folder_vars = ["settings.compiler", "settings.build_type"]
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.user_presets_path = "ConanCMakePresets.json"
        tc.generate()
