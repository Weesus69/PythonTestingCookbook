# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:25:46 2017

@author: Iso Wee
"""
'''Tässä on RomanNumeralTester luokka kääritty(sori paska ilmasu) unittest luokaksi. Tämän etu verrattuna 
assert ajoon on se että nyt jokainen testi ajetaan ja nähdään mitkä failaa ja mitkä ei. Lisäksi assertointi
errori ilmottaa näppärästi miksi arvot eivät täsmää(kts recipe7_legacy)'''

from recipe7 import *
from recipe7_legacy import *
import unittest

if __name__=="__main__":
    tester = RomanNumeralTester()
    suite = unittest.TestSuite()
    for test in [tester.simpe_test, tester.combo_test1, tester.combo_test2, tester.other_test]:
        testcase = unittest.FunctionTestCase(test)
        suite.addTest(testcase)
    unittest.TextTestRunner(verbosity=2).run(suite)