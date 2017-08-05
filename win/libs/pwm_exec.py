#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DESCRIPTION

    PAiP Web Module - JSON

AUTHOR

    Patryk Adamczyk <patrykadamczyk@paip.com.pl>

LICENSE

    PAiP Open Source License

VERSION

    v.0.0.0.1
"""
def execute(command, args = ''):
    """Funkcja Wykonująca Komendy"""
    from subprocess import call
    return call(command + args, shell=True)
