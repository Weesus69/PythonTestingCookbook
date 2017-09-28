# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:06:22 2017

@author: Iso Wee
"""
import unittest


class RomanNumeralKaantaja(object):
    def __init__(self, roomal_numero):
        self.roomal_numero = roomal_numero
        self.roman_dict = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        
        
    def convert_to_decimal(self):
        val = 0
        for char in self.roomal_numero:
            val += self.roman_dict[char]
        return val
        
class RomanNumeralKaantajaTest(unittest.TestCase):
    def test_parsing_millenia(self):
        value = RomanNumeralKaantaja("M")
        self.assertEquals(1000, value.convert_to_decimal())
        
    def test_parsing_halfmillenia(self):
        value = RomanNumeralKaantaja("D")
        self.assertEquals(500, value.convert_to_decimal())
    
    def test_parsing_centuria(self):
        value = RomanNumeralKaantaja("C")
        self.assertEquals(100, value.convert_to_decimal(), "Value is wrong")

    def test_parsing_halfcenturia(self):
        value = RomanNumeralKaantaja("L")
        self.assertEquals(50, value.convert_to_decimal())

    def test_parsing_kyba(self):
        value = RomanNumeralKaantaja("X")
        self.assertEquals(10, value.convert_to_decimal())
        
    def test_parsing_halfkyba(self):
        value = RomanNumeralKaantaja("V")
        self.assertEquals(5, value.convert_to_decimal())
        
    def test_parsing_yks(self):
        value = RomanNumeralKaantaja("I")
        self.assertEquals(1, value.convert_to_decimal())
        
    def test_empty_roman_number(self):
        value = RomanNumeralKaantaja("")
        self.assertTrue(value.convert_to_decimal() == 0)
        self.assertFalse(value.convert_to_decimal() > 0)
    def test_no_number(self):
        value = RomanNumeralKaantaja(None)
        self.assertRaises(TypeError, value.convert_to_decimal)
    
if __name__ == "__main__":
    unittest.main()
        
        