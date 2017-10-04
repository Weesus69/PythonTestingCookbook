# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 12:06:34 2017

@author: Iso Wee
"""
'''Tämä on runner file recipe5.py filelle. Tässä on määritelty kaksi eri testisettiä(suite). Suite1 
käsittää luokan RomanNumeralConverterTest testit ja suite2 luokan Roma...ComboTest testit. Suite taas 
käsittää sekä suite1:n että suite2:n. TextTestRunner:ssa on määritelty nyt että ajetaan suite eli suite1:n
ja suite2:n testit ts. kaikki testit. Näitä runnereita voi tehdä hury mykke eri tarkoituksiin'''


if __name__ == "__main__":
    import unittest    
    from recipe5 import *
    
    suite1 = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralComboTest)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
    