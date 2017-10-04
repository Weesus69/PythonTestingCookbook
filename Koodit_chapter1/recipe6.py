# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 15:53:24 2017

@author: Iso Wee
"""

'''Tässä on kolme eri testisettiä(suite) ja ne kaikki ajetaan erikseen.'''

import unittest

class RomanNumeralConverter(object):
    def __init__(self):
        self.digit_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    
    def convert_to_decimal(self, roman_numeral):
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        return val
        

class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()
    
    def test_parsing_millenia(self):
        self.assertEquals(1000, self.cvt.convert_to_decimal("M"))
        
    def test_parsing_century(self):
        self.assertEquals(100, self.cvt.convert_to_decimal("C"))

    def test_parsing_vuosi(self):
        self.assertEquals(1, self.cvt.convert_to_decimal("I"))

    def test_empty_roman(self):
        self.assertTrue(self.cvt.convert_to_decimal("") == 0)
        self.assertFalse(self.cvt.convert_to_decimal("") > 0)
    
    def test_combo1(self):
        self.assertEquals(4000, self.cvt.convert_to_decimal("MMMM"))
        
    def test_combo2(self):
        self.assertEquals(2505, self.cvt.convert_to_decimal("MMDV"))
        
    def test_combo3(self):
        self.assertEquals(1100, self.cvt.convert_to_decimal("MC"))
        
def high_and_low():
    suite = unittest.TestSuite()
    suite.addTest(RomanNumeralConverterTest("test_parsing_millenia"))
    suite.addTest(RomanNumeralConverterTest("test_parsing_vuosi"))
    return suite

def combos():
    return unittest.TestSuite(map(RomanNumeralConverterTest,["test_combo1", "test_combo2", "test_combo3"]))

def alla():
    return unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterTest)


if __name__=="__main__":
    for suite_func in [high_and_low, combos, alla]:
        print "running test suite: '%s'" % suite_func.func_name
        suite = suite_func()
        unittest.TextTestRunner(verbosity=2).run(suite)

                