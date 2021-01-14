from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool


class OgreConan(ConanFile):
    name = "ogre"
    version = "1.12.10"
    license = "MIT"
    author = "StatelessStudio drew@stateless.studio"
    url = "https://github.com/statelessstudio/ogre-conan"
    description = "3D Graphics Rendering Engine"
    topics = ("graphics", "3d", "3d graphics", "rendering")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "source_uri": "ANY",
        "version_commit": "ANY",
        "cp_bin_dir": "ANY",
        "cp_media_dir": "ANY",
        "disable_plugins": [True, False],
        "OGRE_ASSERT_MODE": "ANY",
        "OGRE_BUILD_COMPONENT_BITES": [True, False],
        "OGRE_BUILD_COMPONENT_CSHARP": [True, False],
        "OGRE_BUILD_COMPONENT_HLMS": [True, False],
        "OGRE_BUILD_COMPONENT_JAVA": [True, False],
        "OGRE_BUILD_COMPONENT_MESHLODGENERATOR": [True, False],
        "OGRE_BUILD_COMPONENT_OVERLAY": [True, False],
        "OGRE_BUILD_COMPONENT_OVERLAY_IMGUI": [True, False],
        "OGRE_BUILD_COMPONENT_PAGING": [True, False],
        "OGRE_BUILD_COMPONENT_PROPERTY": [True, False],
        "OGRE_BUILD_COMPONENT_PYTHON": [True, False],
        "OGRE_BUILD_COMPONENT_RTSHADERSYSTEM": [True, False],
        "OGRE_BUILD_COMPONENT_TERRAIN": [True, False],
        "OGRE_BUILD_COMPONENT_VOLUME": [True, False],
        "OGRE_BUILD_DEPENDENCIES": [True, False],
        "OGRE_BUILD_PLUGIN_BSP": [True, False],
        "OGRE_BUILD_PLUGIN_DOT_SCENE": [True, False],
        "OGRE_BUILD_PLUGIN_OCTREE": [True, False],
        "OGRE_BUILD_PLUGIN_PCZ": [True, False],
        "OGRE_BUILD_PLUGIN_PFX": [True, False],
        "OGRE_BUILD_PLUGIN_STBI": [True, False],
        "OGRE_BUILD_RENDERSYSTEM_D3D11": [True, False],
        "OGRE_BUILD_RENDERSYSTEM_GL": [True, False],
        "OGRE_BUILD_RENDERSYSTEM_GL3PLUS": [True, False],
        "OGRE_BUILD_RTSHADERSYSTEM_SHADERS": [True, False],
        "OGRE_BUILD_SAMPLES": [True, False],
        "OGRE_BUILD_TESTS": [True, False],
        "OGRE_BUILD_TOOLS": [True, False],
        "OGRE_CONFIG_ENABLE_QUAD_BUFFER_STEREO": [True, False],
        "OGRE_CONFIG_FILESYSTEM_UNICODE": [True, False],
        "OGRE_CONFIG_THREADS": "ANY",
        "OGRE_CONFIG_THREAD_PROVIDER": "ANY",
        "OGRE_ENABLE_PRECOMPILED_HEADERS": [True, False],
        "OGRE_INSTALL_PDB": [True, False],
        "OGRE_INSTALL_SAMPLES": [True, False],
        "OGRE_INSTALL_TOOLS": [True, False],
        "OGRE_INSTALL_VSPROPS": [True, False],
        "OGRE_NODELESS_POSITIONING": [True, False],
        "OGRE_PROFILING_REMOTERY_PATH": "ANY",
        "OGRE_RESOURCEMANAGER_STRICT": "ANY",
        "OGRE_STATIC": [True, False],
        "OPENEXR_Half_LIBRARY": "ANY",
        "OPENEXR_Half_LIBRARY_DEBUG": "ANY",
        "OPENEXR_INCLUDE_DIR": "ANY",
        "OPENEXR_Iex_LIBRARY": "ANY",
        "OPENEXR_Iex_LIBRARY_DEBUG": "ANY",
        "OPENEXR_IlmImf_LIBRARY": "ANY",
        "OPENEXR_IlmImf_LIBRARY_DEBUG": "ANY",
        "OPENEXR_IlmThread_LIBRARY": "ANY",
        "OPENEXR_IlmThread_LIBRARY_DEBUG": "ANY",
        "Qt5_DIR": "ANY",
        "SDL2_DIR": "ANY",
        "pugixml_DIR": "ANY"
    }

    default_options = {
        "shared": False,
        "source_uri": "https://github.com/OGRECave/ogre",
        "version_commit": "93d7eb5282d31b956f008a53e837bbb820b34454", # v1.12.10
        "cp_bin_dir": "bin",
        "cp_media_dir": "Media",
        "disable_plugins": False,
        "OGRE_ASSERT_MODE": 1,
        "OGRE_BUILD_COMPONENT_BITES": True,
        "OGRE_BUILD_COMPONENT_CSHARP": False,
        "OGRE_BUILD_COMPONENT_HLMS": False,
        "OGRE_BUILD_COMPONENT_JAVA": False,
        "OGRE_BUILD_COMPONENT_MESHLODGENERATOR": True,
        "OGRE_BUILD_COMPONENT_OVERLAY": True,
        "OGRE_BUILD_COMPONENT_OVERLAY_IMGUI": True,
        "OGRE_BUILD_COMPONENT_PAGING": True,
        "OGRE_BUILD_COMPONENT_PROPERTY": True,
        "OGRE_BUILD_COMPONENT_PYTHON": False,
        "OGRE_BUILD_COMPONENT_RTSHADERSYSTEM": True,
        "OGRE_BUILD_COMPONENT_TERRAIN": True,
        "OGRE_BUILD_COMPONENT_VOLUME": True,
        "OGRE_BUILD_DEPENDENCIES": True,
        "OGRE_BUILD_PLUGIN_BSP": True,
        "OGRE_BUILD_PLUGIN_DOT_SCENE": True,
        "OGRE_BUILD_PLUGIN_OCTREE": True,
        "OGRE_BUILD_PLUGIN_PCZ": True,
        "OGRE_BUILD_PLUGIN_PFX": True,
        "OGRE_BUILD_PLUGIN_STBI": True,
        "OGRE_BUILD_RENDERSYSTEM_D3D11": True,
        "OGRE_BUILD_RENDERSYSTEM_GL": True,
        "OGRE_BUILD_RENDERSYSTEM_GL3PLUS": True,
        "OGRE_BUILD_RTSHADERSYSTEM_SHADERS": True,
        "OGRE_BUILD_SAMPLES": True,
        "OGRE_BUILD_TESTS": False,
        "OGRE_BUILD_TOOLS": True,
        "OGRE_CONFIG_ENABLE_QUAD_BUFFER_STEREO": False,
        "OGRE_CONFIG_FILESYSTEM_UNICODE": True,
        "OGRE_CONFIG_THREADS": 3,
        "OGRE_CONFIG_THREAD_PROVIDER": "std",
        "OGRE_ENABLE_PRECOMPILED_HEADERS": True,
        "OGRE_INSTALL_PDB": True,
        "OGRE_INSTALL_SAMPLES": True,
        "OGRE_INSTALL_TOOLS": True,
        "OGRE_INSTALL_VSPROPS": False,
        "OGRE_NODELESS_POSITIONING": True,
        "OGRE_PROFILING_REMOTERY_PATH": "",
        "OGRE_RESOURCEMANAGER_STRICT": 2,
        "OGRE_STATIC": False,
        "OPENEXR_Half_LIBRARY": "OPENEXR_Half_LIBRARY-NOTFOUND",
        "OPENEXR_Half_LIBRARY_DEBUG": "OPENEXR_Half_LIBRARY_DEBUG-NOTFOUND",
        "OPENEXR_INCLUDE_DIR": "OPENEXR_INCLUDE_DIR-NOTFOUND",
        "OPENEXR_Iex_LIBRARY": "OPENEXR_Iex_LIBRARY-NOTFOUND",
        "OPENEXR_Iex_LIBRARY_DEBUG": "OPENEXR_Iex_LIBRARY_DEBUG-NOTFOUND",
        "OPENEXR_IlmImf_LIBRARY": "OPENEXR_IlmImf_LIBRARY-NOTFOUND",
        "OPENEXR_IlmImf_LIBRARY_DEBUG": "OPENEXR_IlmImf_LIBRARY_DEBUG-NOTFOUND",
        "OPENEXR_IlmThread_LIBRARY": "OPENEXR_IlmThread_LIBRARY-NOTFOUND",
        "OPENEXR_IlmThread_LIBRARY_DEBUG": "OPENEXR_IlmThread_LIBRARY_DEBUG-NOTFOUND",
        "Qt5_DIR": "Qt5_DIR-NOTFOUND",
        "SDL2_DIR": "${ogre-build-dir}/Dependencies/cmake",
        "pugixml_DIR": "${ogre-build-dir}/Dependencies/lib/cmake/pugixml"
    }

    generators = "cmake"

    def system_requirements(self):
        if os_info.is_linux:
            installer = SystemPackageTool()
            installer.install("libgles2-mesa-dev")
            installer.install("libxt-dev")
            installer.install("libxaw7-dev")
            installer.install("nvidia-cg-toolkit")
            installer.install("libsdl2-dev")

    def source(self):
        self.run("git clone " + str(self.options.source_uri))

        if self.options.version_commit:
            print("Checking out version " + self.version + "...")
            self.run(
                "cd ogre && git reset --hard " +
                str(self.options.version_commit)
            )

        print("Checking out submodules...")
        self.run("cd ogre && git submodule update --init --recursive")

    def build(self):
        cmake = CMake(self)

        if self.options.disable_plugins:
            self.options.OGRE_BUILD_PLUGIN_BSP = False
            self.options.OGRE_BUILD_PLUGIN_DOT_SCENE = False
            self.options.OGRE_BUILD_PLUGIN_OCTREE = False
            self.options.OGRE_BUILD_PLUGIN_PCZ = False
            self.options.OGRE_BUILD_PLUGIN_PFX = False
            self.options.OGRE_BUILD_PLUGIN_STBI = False

        for key, value in self.options.items():
            if value is True or value == "True":
                value = "ON"
            elif value is False or value == "False":
                value = "OFF"

            substrpos = value.find('${ogre-build-dir}')
            if substrpos >= 0:
                value = value.replace('${ogre-build-dir}', self.build_folder)

            cmake.definitions[key] = value
            print("Setting cmake [" + key + "] to \"" + value + "\"")

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
            'include/OGRE/RenderSystems',
            'include/OGRE/Threading'
        ]

        if self.options.OGRE_BUILD_COMPONENT_BITES:
            self.cpp_info.includedirs.append('include/OGRE/Bites')

        if self.options.OGRE_BUILD_COMPONENT_HLMS:
            self.cpp_info.includedirs.append('include/OGRE/HLMS')

        if self.options.OGRE_BUILD_COMPONENT_MESHLODGENERATOR:
            self.cpp_info.includedirs.append('include/OGRE/MeshLodGenerator')

        if self.options.OGRE_BUILD_COMPONENT_OVERLAY:
            self.cpp_info.includedirs.append('include/OGRE/Overlay')

        if self.options.OGRE_BUILD_COMPONENT_PAGING:
            self.cpp_info.includedirs.append('include/OGRE/Paging')

        if self.options.OGRE_BUILD_COMPONENT_PROPERTY:
            self.cpp_info.includedirs.append('include/OGRE/Property')

        if self.options.OGRE_BUILD_COMPONENT_RTSHADERSYSTEM:
            self.cpp_info.includedirs.append('include/OGRE/RTShaderSystem')

        if self.options.OGRE_BUILD_COMPONENT_TERRAIN:
            self.cpp_info.includedirs.append('include/OGRE/Terrain')

        if self.options.OGRE_BUILD_COMPONENT_VOLUME:
            self.cpp_info.includedirs.append('include/OGRE/Volume')

        if not self.options.disable_plugins:
            self.cpp_info.includedirs.append('include/OGRE/Plugins')

        self.cpp_info.libs = tools.collect_libs(self)

    def deploy(self):
        self.output.success("Copying OGRE files!")

        if self.options.cp_bin_dir:
            self.copy("*", dst=str(self.options.cp_bin_dir), src="bin")

        if self.options.cp_media_dir:
            self.copy("*", dst=str(self.options.cp_media_dir), src="Media")
