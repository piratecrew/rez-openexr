name = "openexr"

version = "3.1.3"

@early()
def build_requires():
    # check if the system gcc is too old <9
    # then we require devtoolset-9
    from subprocess import check_output
    valid = check_output(r"expr `gcc -dumpversion | cut -f1 -d.` \>= 9 || true", shell=True).strip().decode() == "1"
    if not valid:
        return ["devtoolset-9"]
    return []

build_command = "make -f {root}/Makefile {install}"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    if building:
        env.OpenEXR_ROOT="{root}" # CMake Hint
