"""@lib_build
Script for extracting version control information at compile time

Runs as a PlatformIO library build hook. Can also be ported to other IDEs, or
run manually if another means of modifying the environment is provided.
"""

import sys
import os
import shutil
import datetime
import getpass

Import("env")

# Install GitPython for interacting with remote repositories
try:
    import git
except ImportError:
    env.Execute("$PYTHONEXE -m pip install GitPython")
    import git

################################# BUILD MACROS #################################

# git describe --tags

################################## CONSTANTS ###################################

__version__ = "1.0.0"

############################### HELPER FUNCTIONS ###############################

def getLocalTag(path):
    g = git.Repo(path)
    return [str(next((tag for tag in g.tags if tag.commit == g.head.commit), None))]



################################## MAIN SCRIPT ##################################

# TODO define all the struct constants as macros here
compile_time = datetime.datetime.now(tz=None).strftime("%Y-%m-%dT%H:%MZ")

# Check if in a Git repository: if not, populate with placeholder
path = env['PROJECT_DIR']
try:
    g = git.Repo(path)
    commit_hash = g.head.object.hexsha
    short_hash = g.git.rev_parse(commit_hash, short=7)
    is_dirty = g.is_dirty()
    tag_describe = g.git.describe(tags=True)[0:20]
    author = g.git.show("-s", "--format=%an", commit_hash)[0:20]
except:
    commit_hash = "N/A"
    short_hash = "N/A"
    is_dirty = True
    tag_describe = "N/A"
    author = getpass.getuser()[0:20]

print("****************** VCS - Info ******************")

print("Schema Version: %s" % __version__)
print("Compile Time: %s" % compile_time)
print("Short Hash: %s" % short_hash)
print("Is Dirty: %r" % is_dirty)
print("Tag Description: %r" % tag_describe)
print("Last Author: %r" % author)

print("************************************************")

# Ensure that the VCS block does not get optimised out of the final binary
env.Append(
  LINKFLAGS=[
      "-Wl,--undefined=vcs"
  ]
)