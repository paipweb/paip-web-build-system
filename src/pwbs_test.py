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

    v.0.0.0.1
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
    def test_1(self):
        """pwbs 1"""
        self.assertEqual(pwbs_main(["pwbs.py", "pwbs.tests.TestCase"], False, 1), None)
    def test_2(self):
        """pwbs 2"""
        self.assertEqual(pwbs_execute_multiple(['pwbs.tests.TestCase','pwbs.tests.TestCase'], False), None)
    def test_3(self):
        """pwbs 3"""
        try:
            self.assertEqual(main(["pwbs.py", "--version"]), None)
        except SystemExit:
            pass
    def test_4(self):
        """pwbs 4"""
        try:
            self.assertEqual(main(["pwbs.py", "--help"]), None)
        except SystemExit:
            pass
    def test_5(self):
        """pwbs 5"""
        try:
            self.assertEqual(main(["pwbs.py", "pwbs.tests.TestCase"]), None)
        except SystemExit:
            pass
