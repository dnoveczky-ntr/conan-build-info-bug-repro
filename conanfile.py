from conan import ConanFile
from conan.tools.cmake import cmake_layout

class Playground(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("freetype/2.13.2")

    def layout(self):
        cmake_layout(self)
