# VCS
Tool for embedding version control and status into binary builds with PlatformIO

## Overview

This tool automatically embeds version information into your PlatformIO project.
This info is embedded in the built binaries, and is accessible in your program
through a standard header file. The following information is captured:

### With `Git`

This library is most powerful if using PlatformIO within a `Git` repository, as
exact tag/author/commit info can be pulled: see below:

```json
{
    "schema": 1,
    "compile_time": "2022-01-13T12:03Z",
    "short_hash": "293b1c5",
    "is_dirty": true,
    "tag_describe": "1.0.0-2-g293b1c5",
    "last_author": "James Bennion-Pedley"
}
```

### Without `Git`

The library still works, but does not include the repository fields: the author
is set based on the username of the compiling computer:

```json
{
    "schema": 1,
    "compile_time": "2022-01-13T12:12Z",
    "short_hash": "N/A",
    "is_dirty": true,
    "tag_describe": "N/A",
    "last_author": "james"
}
```

## Usage
Add the library to your project

```ini
lib_deps =
    bojit/VCS@^1.0.0
```

Include the header at least once in the project

```c
#include <VCS.h>
```

Access struct members as follows:

```c
/* Example - print log info at startup (Arduino) */
void setup(void)
{
    Serial.begin(9600);
    Serial.println(vcs.compile_time);
    Serial.println(vcs.last_author);
    Serial.println(vcs.short_hash);
    /* etc... */
}

```
Note that the struct members do not have to be accessed at all to embed versioning into the output binary. Provided the header is included somewhere, the VCS block will be embedded into `firmware.bin`

## Python Helper

Binaries can be checked with a helper Python script that can be used as a command-line tool or a module.
It is located in the root of the library folder, and is called `get_vcs.py`.

Use as follows:

```bash
$ get_vcs.py ./PATH/TO-FIRMWARE.bin
# OR
$ python3 get_vcs.py ./PATH/TO-FIRMWARE.bin

# Pass the 'clean' flag for just VCS output (scripting)
$ get_vcs.py --clean ./PATH/TO-FIRMWARE.bin > something_else

```


## TODO
- The tool currently assumes that the target binary is little-endian. This
  may not be the case for all target platforms