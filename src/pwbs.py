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

    v.0.9.0.1
"""
import sys
from libs.pwm_json import *
from libs.pwm_exec import *
from libs.pwm_pwbs import *
config_file = "pwbs.commands.json"
version = "v.0.9.0.1"
def main(args):
    """Główna Funkcja Programu"""
    verbose_debug_mode = False
    argument_number = 1
    try:
        if args[1] == "--new-config":
            print("PWBS: Generowanie Pustego Pliku Komend")
            dane = []
            write_json(config_file, dane)
            sys.exit()
        elif args[1] == "--version":
            print(version)
            sys.exit()
        elif args[1] == "--help":
            helper = "pwbs [--help] [--version] [--debug] [--new-config] [command]"
            print(helper)
            helper = "System Budowania oparty o wykonywanie komend terminala"
            print(helper)
            sys.exit()
        elif args[1] == "--debug":
            verbose_debug_mode = True
            argument_number = 2
            try:
                test = args[argument_number]
            except Exception:
                print("PWBS: Brak komendy - Uruchamianie 'main'")
    except Exception:
        print("PWBS: Brak komendy - Uruchamianie 'main'")
    pwbs_main(args, verbose_debug_mode, argument_number)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
