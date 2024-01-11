name = "openexr"

version = "3.1.11"

build_requires = [
    "cmake-3.15+<4",
    "gcctoolset-9",
]

requires = [
    "imath-3+<4",
]

build_command = "make -f {root}/Makefile {install}"

tools = [
    "exr2aces",
    "exrenvmap",
    "exrheader",
    "exrinfo",
    "exrmakepreview",
    "exrmaketiled",
    "exrmultipart",
    "exrmultiview",
    "exrstdattr",
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    if building:
        env.OpenEXR_ROOT="{root}" # CMake Hint
