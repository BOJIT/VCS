#!/usr/bin/env python3

"""@get_vcs
Command-line tool for extracting a VCS block from a binary build.
"""

import argparse
# import struct
import sys
import os

# TODO try big and little-endian

################################## CONSTANTS ###################################

__version__ = "1.0.0"

FRAME_START = b'\xFF\xFE\xFD\xFE'
FRAME_END = b'\x01\x02\x03\x04'

################################ Class Definition ##############################

class GetVCS():
    """
        Base class providing methods for processing binary data
    """

    def __init__(self):
        pass

    def _find_all(self, binary, pattern):
        loc = []
        head = 0
        # append first to loc, keep going until find returns -1
        while True:
            l = binary.find(pattern, head)
            if l == -1:
                break
            else:
                head = l + len(pattern)
                loc.append(l)

        return loc

    def getVCS(self, path):
        with open(path, mode='rb') as file:
            file_content = file.read()

            # TODO will this work with little- and big-endian representaions?
            start = self._find_all(file_content, FRAME_START)
            end = self._find_all(file_content, FRAME_END)

############################# Terminal Entry Point #############################

def main(argv=None):
    # Argument parser
    parser = argparse.ArgumentParser(description='get_vcs.py v%s - \
        Tool for extracting VCS blocks from a compiled binary' % __version__, prog='get_vcs')

    parser.add_argument(
        'path',
        help='Path to target binary')

    parser.add_argument(
        '--clean', '-c',
        help='Just print raw block: don\'t add any info/debug logging',
        action='store_true')

    # TODO add options for returning single fieldss

    # Parse argument tree
    nsargs = parser.parse_args(argv)
    args = vars(nsargs)

    if(not(args['clean'])):
        print('get_vcs.py v%s' % __version__)

    # Instantiate base class and call relevant command
    v = GetVCS()

    # Call relevant command
    v.getVCS(args['path'])

    sys.exit(0)


if __name__ == '__main__':
    main()