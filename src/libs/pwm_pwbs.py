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

    v.0.0.0.3
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
            print(unicode("VDM: Command: " + command))
    except Exception:
        command = "main"
        if verbose_debug_mode:
            print(unicode("VDM: Command: " + command))
    try:
        commands = read_json(config_file)
        if verbose_debug_mode:
            print(unicode("VDM: Commands: " + str(commands)))
    except Exception:
        print(unicode("Błąd F1: Błąd odczytywania pliku json"))
        sys.exit()
    if commands == []:
        print(unicode("Błąd F2: Brak pliku "+ config_file +" lub brak komend"))
        if verbose_debug_mode:
            print(unicode("VDM: Config File: " + config_file))
        sys.exit()
    end = False
    for cmd in commands:
        if cmd == command:
            end = True
            if verbose_debug_mode:
                print(unicode("VDM: Test: if " + cmd + "==" + command + "=" + str(end)))
            break
        else:
            if verbose_debug_mode:
                print(unicode("VDM: Test: if " + cmd + "==" + command + "=" + str(end)))
            end = False
    if end:
        if isinstance(commands[command], list):
            if verbose_debug_mode:
                print(unicode("VDM: Test: if isinstance(" + str(commands[command]) + ",list) = " + str(isinstance(commands[command], list))))
            pwbs_execute_multiple(commands[command], verbose_debug_mode)
        else:
            cmd2 = commands[command]
            if verbose_debug_mode:
                print(unicode("VDM: Command to execute: " + cmd2))
            print(unicode("PWBS: Uruchamianie Polecenia '" + command + "'"))
            print(unicode("PWBS: Wykonywanie `" + cmd2 + "`"))
            print(unicode(execute(cmd2)))
    else:
        print(unicode("Błąd A1: Brak Komendy '" + command + "'"))
def pwbs_execute_multiple(commands, vdm):
    """Execute multiple commands"""
    verbose_debug_mode = vdm
    for command in commands:
        if verbose_debug_mode:
            print(unicode("VDM: Multiple commands->" + command))
        try:
            commands3 = read_json(config_file)
            if verbose_debug_mode:
                print(unicode("VDM: Commands3" + str(commands3)))
        except Exception:
            print(unicode("Błąd F1: Błąd odczytywania pliku json"))
            sys.exit()
        if commands3 == []:
            print(unicode("Błąd F2: Brak pliku "+ config_file +" lub brak komend"))
            if verbose_debug_mode:
                print(unicode("VDM: Config File" + config_file))
            sys.exit()
        end = False
        for cmd in commands3:
            if cmd == command:
                end = True
                if verbose_debug_mode:
                    print(unicode("VDM: Test: if " + cmd + "==" + command + "=" + str(end)))
                break
            else:
                if verbose_debug_mode:
                    print(unicode("VDM: Test: if " + cmd + "==" + command + "=" + str(end)))
                end = False
        if end:
            if isinstance(commands3[command], list):
                if verbose_debug_mode:
                    print(unicode("VDM: Test: if isinstance(" + commands[command] + ",list) = " + str(isinstance(commands[command], list))))
                pwbs_execute_multiple(commands3[command])
            else:
                cmd2 = commands3[command]
                if verbose_debug_mode:
                    print(unicode("VDM: Command to execute: " + cmd2))
                print(unicode("PWBS: Uruchamianie Polecenia '" + command + "'"))
                print(unicode("PWBS: Wykonywanie `" + cmd2 + "`"))
                print(unicode(execute(cmd2)))
        else:
            print(unicode("Błąd A1: Brak Komendy '" + command + "'"))
