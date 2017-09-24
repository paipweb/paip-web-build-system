#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DESCRIPTION

    PAiP Web Module - Execute Commands

AUTHOR

    Patryk Adamczyk <patrykadamczyk@paip.com.pl>

LICENSE

    PAiP Open Source License

VERSION

    v.0.0.0.2
"""
def execute(command, args = ''):
    """Funkcja Wykonująca Komendy"""
    from subprocess import call
    if isinstance(command, list):
        retval = ""
        for cmd in command:
            retval += str(call(cmd, shell=True))
        return retval
    else:
        return call(command + args, shell=True)
