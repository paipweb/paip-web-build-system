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

    v.0.9.0.1
"""
import sys
import os
import json
config_file = "pwbs.commands.json"
version = "v.0.9.0.1"
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
verbose_debug_mode = False
arg_num = 1
def pwbs_main(commands2, vdm, argnum):
    """Główna Funkcja Systemu Budowania"""
    verbose_debug_mode = vdm
    arg_num = argnum
    try:
        command = commands2[arg_num]
        if verbose_debug_mode:
            print("VDM: Command: " + command)
    except Exception:
        command = "main"
        if verbose_debug_mode:
            print("VDM: Command: " + command)
    try:
        commands = read_json(config_file)
        if verbose_debug_mode:
            print("VDM: Commands: " + str(commands))
    except Exception:
        print("Błąd F1: Błąd odczytywania pliku json")
        sys.exit()
    if commands == []:
        print("Błąd F2: Brak pliku "+ config_file +" lub brak komend")
        if verbose_debug_mode:
            print("VDM: Config File: " + config_file)
        sys.exit()
    end = False
    for cmd in commands:
        if cmd == command:
            end = True
            if verbose_debug_mode:
                print("VDM: Test: if " + cmd + "==" + command + "=" + str(end))
            break
        else:
            if verbose_debug_mode:
                print("VDM: Test: if " + cmd + "==" + command + "=" + str(end))
            end = False
    if end:
        if isinstance(commands[command], list):
            if verbose_debug_mode:
                print("VDM: Test: if isinstance(" + str(commands[command]) + ",list) = " + str(isinstance(commands[command], list)))
            pwbs_execute_multiple(commands[command], verbose_debug_mode)
        else:
            cmd2 = commands[command]
            if verbose_debug_mode:
                print("VDM: Command to execute: " + cmd2)
            print("PWBS: Uruchamianie Polecenia '" + command + "'")
            print("PWBS: Wykonywanie `" + cmd2 + "`")
            print(execute(cmd2))
    else:
        print("Błąd A1: Brak Komendy '" + command + "'")
def pwbs_execute_multiple(commands, vdm):
    """Execute multiple commands"""
    verbose_debug_mode = vdm
    for command in commands:
        if verbose_debug_mode:
            print("VDM: Multiple commands->" + command)
        try:
            commands3 = read_json(config_file)
            if verbose_debug_mode:
                print("VDM: Commands3" + str(commands3))
        except Exception:
            print("Błąd F1: Błąd odczytywania pliku json")
            sys.exit()
        if commands3 == []:
            print("Błąd F2: Brak pliku "+ config_file +" lub brak komend")
            if verbose_debug_mode:
                print("VDM: Config File" + config_file)
            sys.exit()
        end = False
        for cmd in commands3:
            if cmd == command:
                end = True
                if verbose_debug_mode:
                    print("VDM: Test: if " + cmd + "==" + command + "=" + str(end))
                break
            else:
                if verbose_debug_mode:
                    print("VDM: Test: if " + cmd + "==" + command + "=" + str(end))
                end = False
        if end:
            if isinstance(commands3[command], list):
                if verbose_debug_mode:
                    print("VDM: Test: if isinstance(" + commands[command] + ",list) = " + str(isinstance(commands[command], list)))
                pwbs_execute_multiple(commands3[command])
            else:
                cmd2 = commands3[command]
                if verbose_debug_mode:
                    print("VDM: Command to execute: " + cmd2)
                print("PWBS: Uruchamianie Polecenia '" + command + "'")
                print("PWBS: Wykonywanie `" + cmd2 + "`")
                print(execute(cmd2))
        else:
            print("Błąd A1: Brak Komendy '" + command + "'")


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
