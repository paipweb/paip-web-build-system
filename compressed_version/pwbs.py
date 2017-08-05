#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SYNOPSIS

    pwbs [--help] [--version] [--new-config] [command]

DESCRIPTION

    System Budowania oparty o wykonywanie komend terminala

EXAMPLES

    pwbs test

AUTHOR

    Patryk Adamczyk <patrykadamczyk@paip.com.pl>

LICENSE

    PAiP Open Source License

VERSION

    v.0.0.0.1
"""
import sys
import os
import json
config_file = "pwbs.commands.json"
version = "v.0.0.0.1"
def read_json(nazwapliku):
    """Funkcja odczytuje dane w formacie json z pliku"""
    dane = []
    if os.path.isfile(nazwapliku):
        with open(nazwapliku, "r") as plik:
            dane = json.load(plik)
    return dane
def write_json(nazwapliku, dane):
    """Funkcja zapisuje dane w formacie json do pliku"""
    with open(nazwapliku, "w") as plik:
        json.dump(dane, plik)
    return True
def execute(command, args = ''):
    """Funkcja Wykonująca Komendy"""
    from subprocess import call
    return call(command + args, shell=True)
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
def main(args):
    """Główna Funkcja Programu"""
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
            helper = "pwbs [--help] [--version] [--new-config] [command]"
            print(helper)
            helper = "System Budowania oparty o wykonywanie komend terminala"
            print(helper)
            sys.exit()
    except Exception:
        print("PWBS: Brak komendy - Uruchamianie 'main'")
    pwbs_main(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
