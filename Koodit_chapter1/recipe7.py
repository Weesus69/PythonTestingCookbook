# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:01:34 2017

@author: Iso Wee
"""

class RomanNumeralConverter(object):
    def __init__(self):
        self.digit_map={"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    
    def convert_to_decimal(self, roman_numeral):
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        return val
    