from conans import ConanFile, CMake, tools


class OgreConan(ConanFile):
    name = "ogre"
    version = "1.12.6"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Ogre here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    ogre_version_commit="c1ead4007d6f5552bacd9934a289e4f78b8ecbc2"

    def source(self):
        self.run("git clone C:/Users/Drew/Dev/ogre")

        print("Checking out version " + self.version + "...")
        self.run("cd ogre && git reset --hard " + self.ogre_version_commit)

        print("Checking out submodules...")
        self.run("cd ogre && git submodule update --init --recursive")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="ogre")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="ogre")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = [
            'include',
            'include/OGRE',
            'include/OGRE/Bites',
            'include/OGRE/HLMS',
            'include/OGRE/MeshLodGenerator',
            'include/OGRE/Overlay',
            'include/OGRE/Paging',
            'include/OGRE/Plugins',
            'include/OGRE/Property',
            'include/OGRE/RenderSystems',
            'include/OGRE/RTShaderSystem',
            'include/OGRE/Terrain',
            'include/OGRE/Threading',
            'include/OGRE/Volume'
        ]
        self.cpp_info.libs = tools.collect_libs(self)

