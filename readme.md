# Minimal repro for https://github.com/conan-io/conan-extensions/issues/166

Steps to reproduce:
- Add conancenter as a remote
- `conan install conanfile.py -pr:h windows64.txt -pr:b windows64.txt --settings:host build_type=Release --settings:build build_type=Release --build=never --update -c tools.cmake.cmake_layout:build_folder=build --format=json > conan_build_info.json`

- `conan art:build-info create conan_build_info.json "test_proj" 1.2.3 conancenter --server conancenter --add-cached-deps --with-dependencies`

Conan version used: 2.6.0
