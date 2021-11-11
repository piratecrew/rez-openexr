name = "openexr"

version = "3.1.3"

@early()
def build_requires():
    # check if the system gcc is too old <9
    # then we require devtoolset-9
    requirements = ["cmake-3.15+<4"]
    from subprocess import check_output
    gcc_major = int(check_output(r"gcc -dumpversion | cut -f1 -d.", shell=True).strip().decode())
    if gcc_major < 9:
        requirements.append("devtoolset-9")

    return requirements

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
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    if building:
        env.OpenEXR_ROOT="{root}" # CMake Hint
