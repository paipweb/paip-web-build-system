#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DESCRIPTION

    Skrypt Testujący

AUTHOR

    Patryk Adamczyk <patrykadamczyk@paip.com.pl>

LICENSE

    PAiP Open Source License

VERSION

    v.0.0.0.2
"""
import unittest
from pwbs import *
from libs.pwm_exec import *
from libs.pwm_json import *
from libs.pwm_pwbs import *
class TestExecute(unittest.TestCase):
    """
    Test libs.pwm_exec.execute()
    """
    def test_type(self):
        """execute("echo Hello World") returns an integer return code"""
        self.assertEqual(type(execute("echo Hello World")), int)

class TestPWBS(unittest.TestCase):
    """
    Test libs.pwm_pwbs module
    """
    def test_a1(self):
        """pwbs 1"""
        self.assertEqual(pwbs_main(["pwbs.py", "pwbs.tests.TestCase"], False, 1), None)
    def test_a2(self):
        """pwbs 2"""
        self.assertEqual(pwbs_execute_multiple(['pwbs.tests.TestCase','pwbs.tests.TestCase'], False), None)
    def test_a3(self):
        """pwbs 3"""
        try:
            self.assertEqual(main(["pwbs.py", "--version"]), None)
        except SystemExit:
            pass
    def test_a4(self):
        """pwbs 4"""
        try:
            self.assertEqual(main(["pwbs.py", "--help"]), None)
        except SystemExit:
            pass
    def test_a5(self):
        """pwbs 5"""
        try:
            self.assertEqual(main(["pwbs.py", "pwbs.tests.TestCase"]), None)
        except SystemExit:
            pass
    def test_a6(self):
        """pwbs 6"""
        try:
            self.assertEqual(main(["pwbs.py", "--new-config"], True), None)
        except SystemExit:
            pass
    def test_a7(self):
        """pwbs 7"""
        try:
            self.assertEqual(main(["pwbs.py", "--debug", "test"], True), None)
        except SystemExit:
            pass
    def test_a8(self):
        """pwbs 8"""
        try:
            self.assertEqual(main(["pwbs.py", "--debug"], True), None)
        except SystemExit:
            pass
    def test_a9(self):
        """pwbs 9"""
        try:
            self.assertEqual(main(["pwbs.py"], True), None)
        except SystemExit:
            pass
    def test_b0(self):
        """pwbs 10"""
        try:
            self.assertEqual(main(["pwbs.py", "--debug", "x"], True), None)
        except SystemExit:
            pass
    def test_b1(self):
        """pwbs 11"""
        config_file = "pwbs.commands.json"
        commands = read_json(config_file)
        self.assertEqual(write_json(config_file, commands), True)
        commands2 = read_json(config_file)
        self.assertEqual(commands == commands2, True)
