# ogre-conan (Developer)

## Updating Ogre Version

- Replace all instances of old version with new version
  - In conanfile.py
  - In README.md
- Replace version commit hash
- Check for new/changed CMAKE options

## Building/Testing

`conan create . demo/testing`

## Uploading

https://docs.conan.io/en/latest/uploading_packages/bintray/uploading_bintray.html

`conan user -p BINTRAY_API_KEY_HERE -r ogre statelessstudio`

`conan upload ogre/VERSION@demo/testing --all -r=ogre`
