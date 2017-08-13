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

    v.0.0.0.4
"""
import sys
from .pwm_json import *
from .pwm_exec import *
config_file = "pwbs.commands.json"
verbose_debug_mode = False
arg_num = 1
def pwbs_main(commands2, vdm, argnum):
    """Główna Funkcja Systemu Budowania"""
    verbose_debug_mode = vdm
    arg_num = argnum
    try:
        command = commands2[arg_num]
        if verbose_debug_mode:
            print(u"VDM: Command: " + command)
    except Exception:
        command = "main"
        if verbose_debug_mode:
            print(u"VDM: Command: " + command)
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
    end = False
    for cmd in commands:
        if cmd == command:
            end = True
            if verbose_debug_mode:
                print(u"VDM: Test: if " + cmd + "==" + command + "=" + str(end))
            break
        else:
            if verbose_debug_mode:
                print(u"VDM: Test: if " + cmd + "==" + command + "=" + str(end))
            end = False
    if end:
        if isinstance(commands[command], list):
            if verbose_debug_mode:
                print(u"VDM: Test: if isinstance(" + str(commands[command]) + ",list) = " + str(isinstance(commands[command], list)))
            pwbs_execute_multiple(commands[command], verbose_debug_mode)
        else:
            cmd2 = commands[command]
            if verbose_debug_mode:
                print(u"VDM: Command to execute: " + cmd2)
            print(u"PWBS: Uruchamianie Polecenia '" + command + "'")
            print(u"PWBS: Wykonywanie `" + cmd2 + "`")
            print(execute(cmd2))
    else:
        try:
            print(u"Błąd A1: Brak Komendy '" + command + "'")
        ## Tested manually
        except UnicodeEncodeError: # pragma: no cover
            print(u"Error A1: No command '" + command + "'")
def pwbs_execute_multiple(commands, vdm):
    """Execute multiple commands"""
    verbose_debug_mode = vdm
    for command in commands:
        if verbose_debug_mode:
            print(u"VDM: Multiple commands->" + command)
        try:
            commands3 = read_json(config_file)
            if verbose_debug_mode:
                print(u"VDM: Commands3" + str(commands3))
        except Exception:  # pragma: no cover
            try:
                print(u"Błąd F1: Błąd odczytywania pliku json")
            except UnicodeEncodeError:
                print("Error F1: Can't read json file")
            sys.exit()
        ## Tested manually
        if commands3 == []: # pragma: no cover
            try:
                print(u"Błąd F2: Brak pliku "+ config_file +" lub brak komend")
            except UnicodeEncodeError:
                print("Error F2: Can't read" + config_file + " file or no commands")
            if verbose_debug_mode:
                print(u"VDM: Config File" + config_file)
            sys.exit()
        end = False
        for cmd in commands3:
            if cmd == command:
                end = True
                if verbose_debug_mode:
                    print(u"VDM: Test: if " + cmd + "==" + command + "=" + str(end))
                break
            else:
                if verbose_debug_mode:
                    print(u"VDM: Test: if " + cmd + "==" + command + "=" + str(end))
                end = False
        if end:
            if isinstance(commands3[command], list):
                if verbose_debug_mode:
                    print(u"VDM: Test: if isinstance(" + str(commands3[command]) + ",list) = ", isinstance(commands3[command], list))
                pwbs_execute_multiple(commands3[command], verbose_debug_mode)
            else:
                cmd2 = commands3[command]
                if verbose_debug_mode:
                    print(u"VDM: Command to execute: " + cmd2)
                print(u"PWBS: Uruchamianie Polecenia '" + command + "'")
                print(u"PWBS: Wykonywanie `" + cmd2 + "`")
                print(execute(cmd2))
        else:
            try:
                print(u"Błąd A1: Brak Komendy '" + command + "'")
            ## Tested manually
            except UnicodeEncodeError: # pragma: no cover
                print(u"Error A1: No command '" + command + "'")
