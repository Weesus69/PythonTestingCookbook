# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:24:12 2017

@author: Iso Wee
"""
'''Tässä ideana on luoda metodi joka käy läpi testikeissit, jotka on määritettynä tuplena. Varmaan ihan jees
mutta ei ny aukee'''

import unittest

class RomanNumeralConverter(object):
    def __init__(self):
        self.digit_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    
    def convert_to_decimal(self, roman_numeral):
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        if val > 4000:
            raise Exception("Doesn't passaa yli 4000 arvot")
        return val
        
    def convert_to_roman(self, decimal):
        if decimal > 4000:
            raise Exception("Doesn't käy yli 4000 arvot")
        val = ""
        mappers = [(1000, "M"), (500, "D"), (100, "C"), (50, "L"), (10, "X"), (5, "V"), (1, "I")]
        for (rom_num, rom_dec) in mappers:
            while decimal >= rom_dec:
                val += rom_num
                decimal -= rom_dec
        return val

class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()
        
    def test_edges(self):
        r = self.cvt.convert_to_roman
        d = self.cvt.convert_to_decimal
        edges = [("equals", r, "I", 1), ("equals", r, "", 0), ("equals", r, "", -1), ("equals", r, "MMMM", 4000),
                 ("raises", r, Exception, 4001), ("equals", d, 1, "I"), ("equals", d, 0, ""), ("equals", d, 4000, "MMMM"),
                ("raises", d, Exception, "MMMMI")]
        [self.checkout_edge(edge) for edge in edges]
        
    def test_tiers(self):
        r = self.cvt.convert_to_roman
        edges = [("equals", r, "V", 5), ("equals", r, "VIIII", 9), ("equals", r, "X", 10),
                 ("equals", r, "XI", 11), ("equals", r, "XXXXVIIII", 49), ("equals", r, "L", 50),
                ("equals", r, "LI", 51), ("equals", r, "LXXXXVIIII", 99), ("equals", r, "C", 100),
                ("equals", r, "CI", 101), ("equals", r, "CCCCLXXXXVIIII", 499), ("equals", r, "D", 500),
                ("equals", r, "DI", 501), ("equals", r, "M", 1000)]
        [self.checkout_edge(edge) for edge in edges]
        
    def test_bad_inputs(self):
        r = self.cvt.convert_to_roman
        d = self.cvt.convert_to_decimal
        edges = [("equals", r, "", None), ("equals", r, "I", 1.2), ("raises", d, TypeError, None),
                 ("raises", d, TypeError, 1.2)]
        [self.checkout_edge(edge) for edge in edges]
        
    def checkout_edge(self, edge):
        if edge[0] == "equals":
            f, output, inputt = edge[1], edge[2], edge[3]
            print ("Converting %s to %s..." % (inputt, output))
            self.assertEquals(output, f(inputt))
        elif edge[0] == "raises":
            f, exception, args = edge[1], edge[2], edge[3:]
            print ("Converting %s, expecting %s" % (args, exception))
            self.assertEquals(exception, f, *args)
            
if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralTest)
    unittest.TextTestRunner(verbosity=2).run(suite)