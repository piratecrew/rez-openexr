name = "openexr"

version = "3.1.3"

build_command = "make -f {root}/Makefile {install}"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    if building:
        env.OpenEXR_ROOT="{root}" # CMake Hint
