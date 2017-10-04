# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 11:56:30 2017

@author: Iso Wee
"""
'''Tälle koodille on oma ajuritiedost recipe5_runner.py
Perusidea tässä on kuitenkin että luodaan kaksi eri testisettiä(suite), joihin voidaan määritellä
erilaisia testikeissejä. Varsinaisessa runnerfilessa on sitten toteutus sille miten näitä ajellaan'''


import unittest

class RomanNumeralConverter(object):
    def __init__(self):
        #self.roman_numeral = roman_numeral
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
        
class RomanNumeralComboTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()
     
    def test_multi_millenia(self):
        self.assertEquals(4000, self.cvt.convert_to_decimal("MMMM"))
        
    def test_twohundredandfive(self):
        self.assertEquals(205, self.cvt.convert_to_decimal("CCV"))
