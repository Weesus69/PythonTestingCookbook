# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:52:05 2017

@author: Iso Wee
"""
'''Tässä ajetaan kaksi testiä mutta kummassakin assertoidaan useampaa asiaa. Ajossa tämä näkyy siten että
yksi testi failaa. Eikä lopputulema muutenkaan ole kovin selvä, koska miksi failaa? Missä bugi?'''

import unittest
from recipe8 import *

class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()
    
    def test_convert_to_decimal(self):
        self.assertEquals(0, self.cvt.convert_to_decimal(""))
        self.assertEquals(1, self.cvt.convert_to_decimal("I"))
        self.assertEquals(2010, self.cvt.convert_to_decimal("MMX"))
        self.assertEquals(4000, self.cvt.convert_to_decimal("MMMM"))
        
    def test_convert_to_roman(self):
        self.assertEquals("", self.cvt.convert_to_roman(0))
        self.assertEquals("II", self.cvt.convert_to_roman(2))
        self.assertEquals("V", self.cvt.convert_to_roman(5))
        self.assertEquals("XII", self.cvt.convert_to_roman(12))
        self.assertEquals("MMX", self.cvt.convert_to_roman(2010))
        self.assertEquals("MMMM", self.cvt.convert_to_roman(4000))

if __name__=="__main__":
    unittest.main()