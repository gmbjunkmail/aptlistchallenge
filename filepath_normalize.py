#!/usr/bin/env python2

import sys
import re


def main():
    raw = sys.stdin.read()
    print format_filepath(raw)


def format_filepath(raw):
    """Return a formatted version of the raw string by removing . and ..
    such that . are removed and .. evaluates to the parent directory.
    The raw input is assumed to be a UNIX file path.

    >>> format_filepath('foo/./bar/../baz.txt')
    'foo/baz.txt'

    >>> format_filepath('foo//bar')
    'foo//bar'
    """

    # add a leading a trailing slash to avoid edge cases
    formatted = "/" + raw.strip() + "/"

    # change / to // to avoid edge cases
    formatted = re.sub(r"/", "//", formatted)

    # remove empty dot characters, ie "//foo//.//" becomes "//foo//"
    formatted = re.sub(r"(?:/)(\./)", "", formatted)

    # remove parent directory representation
    # ie "//foo//bar//..//baz//..//" becomes "//foo//"
    # repeats for each overlapping /../
    # ie "//foo//bar//baz//..//..//" needs to loop twice
    formatted_loop = ''
    while formatted != formatted_loop:
        formatted_loop = formatted
        formatted = re.sub(r"(?:/)([^(/|\.\.)]*//\.\./)", "", formatted_loop)

    # change // back to /
    formatted = re.sub(r"//", "/", formatted)

    # remove the leading and trailing slashes
    formatted = formatted[1:-1]

    return formatted


if __name__ == "__main__":
    main()
