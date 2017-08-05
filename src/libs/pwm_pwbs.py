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

    v.0.0.0.2
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
