#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DESCRIPTION

    PAiP Web Module - PAiP Web Build System

AUTHOR

    Patryk Adamczyk <patrykadamczyk@paip.com.pl>

LICENSE

    PAiP Open Source License

VERSION

    v.0.0.0.1
"""
import sys
from .pwm_json import *
from .pwm_exec import *
config_file = "pwbs.commands.json"
def pwbs_main(commands2):
    """Główna Funkcja Systemu Budowania"""
    try:
        command = commands2[1]
    except Exception:
        command = "main"
    try:
        commands = read_json(config_file)
    except Exception:
        print("Błąd F1: Błąd odczytywania pliku json")
        sys.exit()
    if commands == []:
        print("Błąd F2: Brak pliku "+ config_file +" lub brak komend")
        sys.exit()
    end = False
    for cmd in commands:
        if cmd == command:
            end = True
        else:
            end = False
    if end:
        cmd2 = commands[command]
        print("PWBS: Uruchamianie Polecenia '" + command + "'")
        print("PWBS: Wykonywanie `" + cmd2 + "`")
        print(execute(cmd2))
    else:
        print("Błąd A1: Brak Komendy '" + command + "'")
