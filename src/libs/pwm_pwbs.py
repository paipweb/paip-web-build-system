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

    v.0.0.0.5
"""
import sys
from .pwm_json import *
from .pwm_exec import *
config_file = "pwbs.commands.json"
verbose_debug_mode = False
def pwbs_main(arguments, verbose_debug_mode):
    """Główna Funkcja Systemu Budowania"""
    try:
        commands = read_json(config_file)
        if verbose_debug_mode:
            print(u"VDM: Commands: " + str(commands))
    except Exception: # pragma: no cover
        try:
            print(u"Błąd F1: Błąd odczytywania pliku json")
        except UnicodeEncodeError:
            print("Error F1: Can't read json file")
        sys.exit()
    ## Tested manually
    if commands == []: # pragma: no cover
        try:
            print(u"Błąd F2: Brak pliku "+ config_file +" lub brak komend")
        except UnicodeEncodeError:
            print("Error F2: Can't read" + config_file + " file or no commands")
        if verbose_debug_mode:
            print(u"VDM: Config File: " + config_file)
        sys.exit()
    special_commands = ['--new-config', '--version', '--help', '--debug']
    s = False
    c = False
    if verbose_debug_mode:
        print(u"VDM: Arguments: " + str(arguments[1:]))
    for arg in arguments[1:]:
        s = True
        if verbose_debug_mode:
            print(u"VDM: Test: if " + arg + " in " + str(commands) + " or " + str(special_commands))
        if arg in special_commands:
            verbose_debug_mode = pwbs_execute_scommand(arg, verbose_debug_mode)
        elif arg in commands:
            c = True
            if isinstance(commands[arg], list):
                if verbose_debug_mode:
                    print(u"VDM: Test: if isinstance(" + str(commands[arg]) + ",list) = " + str(isinstance(commands[arg], list)))
                verbose_debug_mode = pwbs_execute_multicommand(commands[arg], verbose_debug_mode, commands, special_commands)
            else:
                cmd2 = commands[arg]
                if verbose_debug_mode:
                    print(u"VDM: Command to execute: " + cmd2)
                print(u"PWBS: Uruchamianie Polecenia '" + arg + "'")
                print(u"PWBS: Wykonywanie `" + cmd2 + "`")
                execute(cmd2)
        else:
            c = True
            print(u"PWBS: Brak Komendy " + arg)
    if (s is False) or (c is False):
        print(u"PWBS: Brak komendy - Uruchamianie 'main'")
        if "main" in commands:
            if isinstance(commands['main'], list):
                if verbose_debug_mode:
                    print(u"VDM: Test: if isinstance(" + str(commands['main']) + ",list) = " + str(isinstance(commands['main'], list)))
                verbose_debug_mode = pwbs_execute_multicommand(commands['main'], verbose_debug_mode, commands, special_commands)
            else:
                cmd2 = commands["main"]
                if verbose_debug_mode:
                    print(u"VDM: Command to execute: " + cmd2)
                print(u"PWBS: Uruchamianie Polecenia '" + "main" + "'")
                print(u"PWBS: Wykonywanie `" + cmd2 + "`")
                execute(cmd2)
        else:
            print(u"PWBS: Brak komendy 'main'")

def pwbs_execute_scommand(command, vdm):
    """Funkcja wykonująca zadanie specjalne"""
    verbose_debug_mode = vdm
    if command == "--new-config":
        print("PWBS: Generowanie Pustego Pliku Komend")
        dane = []
        if not special: # pragma: no cover
            write_json(config_file, dane)
        sys.exit()
    elif command == "--version":
        version = "v.0.9.1.0"
        print(version)
        sys.exit()
    elif command == "--help":
        helper = "pwbs [--help] [--version] [--debug] [--new-config] [command]"
        print(helper)
        helper = "System Budowania oparty o wykonywanie komend terminala"
        print(helper)
        sys.exit()
    elif command == "--debug":
        try:
            print(u"PWBS: Włączanie Trybu Debugowania")
        except UnicodeEncodeError:
            print("PWBS: Enabling Debug Mode")
        verbose_debug_mode = True
    return verbose_debug_mode
def pwbs_execute_multicommand(command, verbose_debug_mode, commands, special_commands):
    """Funkcja wykonująca zadanie wielofunkcyjne"""
    if command is []:
        return 0
    special_commands = ['--new-config', '--version', '--help', '--debug']
    for arg in command:
        if verbose_debug_mode:
            print(u"VDM: Test: if " + arg + " in " + str(commands) + " or " + str(special_commands))
        if arg in special_commands:
            verbose_debug_mode = pwbs_execute_scommand(arg, verbose_debug_mode)
        elif arg in commands:
            if isinstance(commands[arg], list):
                if verbose_debug_mode:
                    print(u"VDM: Test: if isinstance(" + str(commands[arg]) + ",list) = " + str(isinstance(commands[arg], list)))
                verbose_debug_mode = pwbs_execute_multicommand(commands[arg], verbose_debug_mode, commands, special_commands)
            else:
                cmd2 = commands[arg]
                if verbose_debug_mode:
                    print(u"VDM: Command to execute: " + cmd2)
                print(u"PWBS: Uruchamianie Polecenia '" + arg + "'")
                print(u"PWBS: Wykonywanie `" + cmd2 + "`")
                execute(cmd2)
        else:
            print(u"PWBS: Brak Komendy " + arg)
