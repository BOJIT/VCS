"""@lib_build
Script for extracting version control information at compile time

Runs as a PlatformIO library build hook. Can also be ported to other IDEs, or
run manually if another means of modifying the environment is provided.
"""

import datetime
import getpass

Import("env")

# Install GitPython for interacting with remote repositories
try:
    import git
except ImportError:
    env.Execute("$PYTHONEXE -m pip install GitPython")
    import git

################################## CONSTANTS ###################################

__version__ = "1.0.0"

################################## MAIN SCRIPT ##################################

compile_time = datetime.datetime.now(tz=None).strftime("%Y-%m-%dT%H:%MZ")

# Check if in a Git repository: if not, populate with placeholder
path = env["PROJECT_DIR"]
try:
    g = git.Repo(path, search_parent_directories=True)
    commit_hash = g.head.object.hexsha
    short_hash = g.git.rev_parse(commit_hash, short=7)[0:10]
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

# Append macros to global build environment
env.Append(
    CPPDEFINES=[
        ("__VCS_COMPILE_TIME", '\\"' + compile_time + '\\"'),
        ("__VCS_SHORT_HASH", '\\"' + short_hash + '\\"'),
        ("__VCS_IS_DIRTY", "1" if is_dirty else "0"),
        ("__VCS_TAG_DESCRIBE", '\\"' + tag_describe + '\\"'),
        ("__VCS_LAST_AUTHOR", '\\"' + author + '\\"'),
    ]
)

# Ensure that the VCS block does not get optimised out of the final binary
env.Append(LINKFLAGS=["-Wl,--undefined=vcs"])
