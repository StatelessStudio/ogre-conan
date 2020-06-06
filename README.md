# ogre-conan
Conan recipe for Ogre3d

**This conan package exposes (nearly) all of Ogre's cmake options. If you'd like to customize the build beyond the defaults, read [Customizing Ogre](#customizing-ogre) before installing!**

## Step 1 - Set remote

```
conan remote add ogre https://api.bintray.com/conan/statelessstudio/ogre
```

## Step 2 - Add to CMake

Add the following to a root-level `CMakeLists.txt`:

```cmake
cmake_minimum_required(VERSION 2.8.12)

project(OgreExample)

include(dependencies/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB source_files
    "**/*.h"
    "**/*.cpp"
)

add_executable (OgreExample ${source_files})
target_link_libraries(OgreExample ${CONAN_LIBS})

```

## Step 3 - Option 1 - (Recommended) Install with bin & media directories

**If you're just getting started with Ogre, you should probably use this step!**

If you'd rather copy the `bin/` and `Media/` directories yourself, you can skip this step.

In addition to building Ogre & it's dependencies, this will also add the `bin/` and example `Media/` directory to your project.

```
conan install ogre/1.12.6@demo/testing --build ogre
```

### Custom bin directory

If you'd like to change the `bin/` or `Media/` directory, or set a custom build directory, you can pass directoreis to the `ogre:cp_bin_dir` and `ogre:cp_media_dir` options:

```
conan install ogre/1.12.6@demo/testing --build ogre -o ogre:cp_bin_dir=build/x64-Release -o ogre:cp_media_dir=build/Media
```

### Why doesn't installing with a conanfile copy the bin & media directories?

See [this conan.io issue](https://github.com/conan-io/conan/issues/7126#issuecomment-637029596)

## Step 3 - Option 2 - Add to conanfile.txt

If you don't need the `Media/` directory, and would rather copy the bin folder contents (`.dll`s, Ogre Tools, etc) manually, you can install Ogre without:

Add the following to a root-level `conanfile.txt`:

```
[requires]
ogre/1.12.6@demo/testing

[options]

[generators]
cmake

```

Then run the following:

`mkdir dependencies && cd dependencies`

`conan install .. --build ogre`

### Manually copying bin & media

If you skipped step 3, the bin and media directory are all there, they just haven't been copied to your project. You can find these in `~/.conan/data/ogre/1.12.6/demo/testing/package/SOMEHASH/` or `C:/Users/SOMEUSERNAME/.conan/data/...` on Windows.

## Next steps

You can now include Ogre files in your project:

`src/main.cpp`
```cpp
#include <Ogre.h>
#include <Bites/OgreApplicationContext.h>
#include <Bites/OgreInput.h>
#include <RTShaderSystem/OgreRTShaderSystem.h>
```

## Customizing Ogre

Besides a few exceptions, you can set nearly all of Ogre's cmake options. We've removed a few options (such as directories and cmake settings) because they would break the conan integration.

**Not all options have been tested. Please [report any issues](https://github.com/StatelessStudio/ogre-conan/issues) you find!**

The options match ogre's cmake names exactly. You can browse all of the options with the command `conan inspect ogre/1.12.6@demo/testing`

### CLI Method (Option 1 above)

If you are using option 1 above, pass additional `-o ogre:` parameters to the command:

`conan install ogre/1.12.6@demo/testing --build ogre -o ogre:OGRE_BUILD_COMPONENT_BITES=False -o ogre:Qt5_DIR=C:/qt5/`

### Conanfile.txt Method (Option 2 above)

If you are using option 2 above, add the options to your conanfile before you build:

`conanfile.txt`
```
[requires]
ogre/1.12.6@demo/testing

[options]
ogre:BUILD_COMPONENT_BITES=False
ogre:Qt5_DIR=C:/qt5/
...
```

## A note on dependencies

By default, ogre-conan will use Ogre's default cmake build chain & dependencies. If you'd like to use system-wide Ogre dependencies through conan, you should set `ogre:OGRE_BUILD_DEPENDENCIES=False`, and install each of Ogre's dependencies manually.

## Disabling plugins

If you don't want to build Ogre with any plugins, set `ogre:disable_plugins=True`

## Changing the Ogre repo or version

### Repo URI

By default, the ogre uri is `https://github.com/ogrecave/ogre`. You can use a differant fork with the option `ogre:source_uri`

### Version Commit

The version commit is a commit hash that is tagged with each ogre version. You can find the version commit for each hash on [Ogre's Releases page](https://github.com/OGRECave/ogre/releases).

Set the hash like this: `ogre:version_commit=c1ead4007d6f5552bacd9934a289e4f78b8ecbc2`.

If you'd like skip version checkout, you can set `ogre:version_commit` to `False`, and leave the repo on the latest development changes (**Dangerous**)
