#!/usr/bin/env python
# Copyright (c) 2012 Eduardo Felipe Castegnaro, http://github.com/edufelipe/
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import subprocess
import os
import re
import sys


def _colored():
    """Code inspired by http://pypi.python.org/pypi/termcolor"""
    ATTRIBUTES = {"reverse": 7, "dark": 2, "underline": 4, "bold": 1}
    HIGHLIGHTS = {"on_cyan": 46, "on_white": 47, "on_grey": 40, "on_red": 41,
        "on_yellow": 43, "on_blue": 44, "on_magenta": 45, "on_green": 42}
    COLORS = {"blue": 34, "grey": 30, "yellow": 33, "green": 32, "cyan": 36,
        "magenta": 35, "white": 37, "red": 31}
    SHOULD_COLOR = sys.stdout.isatty() and os.getenv("ANSI_COLORS_DISABLED") is None

    def _cached_colored(text, color=None, on_color=None, attrs=[]):
        if SHOULD_COLOR:
            fmt_str = "\033[%dm%s"
            if color: text = fmt_str % (COLORS[color], text)
            if on_color: text = fmt_str % (HIGHLIGHTS[on_color], text)
            for attr in attrs: text = fmt_str % (ATTRIBUTES[attr], text)
            text += "\033[0m"
        return text

    return _cached_colored

colored = _colored()


def format_entry(max_length_destination, origin, destination, fstype, options):
    # Format options and treat `bind` as an fstype.
    options = sorted(o.strip() for o in options.split(",") if o)
    if fstype == 'none' and 'bind' in options:
        fstype = options.pop(options.index('bind'))

    text = colored("%-*s"%(max_length_destination, destination), "cyan", attrs=["bold"]) + " -> "
    text += colored(origin, "yellow", attrs=["bold"]) if "/" in origin else origin

    if fstype:
        text += " [%s]" % colored(fstype, "magenta", attrs=["bold"])
    if options:
        for access in ('ro', 'rw'):
            if access in options:
                options.remove(access)
                options.insert(0, colored(access, "blue"))
        text += " (%s)" % ", ".join(options)

    return destination.lower(), text


def mount_regex():
    """Deal with Darwin and Linux"s idiosyncrasies on mount formatting."""
    if sys.platform.startswith("linux"):
        return re.compile(r"""^(?P<origin>.*?)\son\s(?P<destination>.*?)\s
type\s(?P<fstype>[\w.-]+)\s\((?P<options>.*)\)$""", re.X)
    elif sys.platform.startswith("darwin"):
        return re.compile(r"""^(?P<origin>.*?)\son\s(?P<destination>.*?)\s
\((?P<fstype>\w+),?\s?(?P<options>.*)\)$""", re.X)
    else:
        raise RuntimeError("Unkwown platform")


def mountpoints():
    """List mountpoints of the system."""
    return subprocess.getoutput("mount").splitlines()


def formated(mount_list):
    """Format mountpoints in a prettier way."""
    regex = mount_regex()
    matches = [regex.match(mountpoint) for mountpoint in mount_list]
    mountpoint_destinations = [m.group("destination") for m in matches]
    max_length_destination = max([len(s) for s in mountpoint_destinations])

    for mountpoint in mount_list:
        match = regex.match(mountpoint)
        if match:
            yield format_entry(max_length_destination, **match.groupdict())
        else:
            yield mountpoint


def print_formatted_mountpoints():
    for _, mountpoint in sorted(formated(mountpoints()), key=lambda x: x[0]):
        print(mountpoint)


if __name__ == "__main__":
    print_formatted_mountpoints()
