"""@lib_build
Script for extracting version control information at compile time

Runs as a PlatformIO library build hook. Can also be ported to other IDEs, or
run manually if another means of modifying the environment is provided.
"""

import sys
import os
import shutil

Import("env")

# Install GitPython for interacting with remote repositories
try:
    import git
except ImportError:
    env.Execute("$PYTHONEXE -m pip install GitPython")
    import git

################################# BUILD MACROS #################################

# git rev-parse --short HEAD
# git describe --tags

################################## CONSTANTS ###################################

# KERNEL_URL = "https://github.com/FreeRTOS/FreeRTOS-Kernel.git"
# KERNEL_PATH = os.path.realpath('./FreeRTOS-Kernel')

############################### HELPER FUNCTIONS ###############################

def getLocalTag(path):
    g = git.Repo(path)
    return [str(next((tag for tag in g.tags if tag.commit == g.head.commit), None))]

################################## MAIN SCRIPT ##################################

print("Hello World!")

# TODO define all the struct constants as macros here

# Ensure that the VCS block does not get optimised out of the final binary
env.Append(
  LINKFLAGS=[
      "-Wl,--undefined=vcs"
  ]
)