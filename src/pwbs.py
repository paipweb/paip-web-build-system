#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SYNOPSIS

    pwbs [--help] [--version] [--debug] [--new-config] [command]

DESCRIPTION

    System Budowania oparty o wykonywanie komend terminala

EXAMPLES

    pwbs test

AUTHOR

    Patryk Adamczyk <patrykadamczyk@paip.com.pl>

LICENSE

    PAiP Open Source License

VERSION

    v.0.9.1.0
"""
import sys
from libs.pwm_json import *
from libs.pwm_exec import *
from libs.pwm_pwbs import *
version = "v.0.9.1.0"
config_file = "pwbs.commands.json"
def main(args, special=False):
    """Główna Funkcja Programu"""
    verbose_debug_mode = False
    print("PAiP Web Build System " + version)
    pwbs_main(args, verbose_debug_mode)
    sys.exit()

if __name__ == '__main__': # pragma: no cover
    sys.exit(main(sys.argv))
