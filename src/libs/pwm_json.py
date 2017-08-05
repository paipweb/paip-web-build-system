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
import os
import json

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
