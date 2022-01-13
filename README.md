# VCS
Tool for embedding version control and status into binary builds with PlatformIO

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