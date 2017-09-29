# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:33:33 2017

@author: Iso Wee
"""

'''Tässä luodaan ensin luokka RomanNumeralKaantaja. Siellä on dictionary roman_dict jossa määritellään
roomalaiset numerot ja niiden länkkärivastine. Lisäksi funktio convert_to_decimal tallentaa 
länkkäriluvun eli dictionaryn arvon val -muuttujaan joka palautetaan. Sitten luodaan tämän luokan pohjalta
testi luokka(luokan nimi.Test) ja importoidaan unittest moduli. Testiluokassa määritellään
setUp metodi ja tearDown metodi jotka ajetaan aina ennen testiä ja testin jälkeen. Ensiksi mainittu
alustaa testin tai tekee tarvittavat alkusäädöt, tässä tapauksessa luo kertakäyttöinstanssin testattavasta
luokasta. Jälkimmäinen "tuhoaa" sen eli asettaa instanssin arvon 'None':ksi. Lisäksi testiluokassa
luodaan testejä eli testimetodeja ja nämä tunnistaa siitä että ne alkavat test -sanalla. Nämä
ajetaan sitten kun tämä file ajetaan. Testit testaa että roomalainen numero ja länkkäriarvo mäppäytyvät
oikein. Lisäksi testataan nolla arvo ja tyhjä arvo. Jotta testit saadaan ajoon pitää lopuksi määrittää
if __name__ == "__main__":
    unittest.main()
Jos tätä ei ole niin sitten varsinainen ajo suorittaa vain pääluokkaa eikä aja testejä'''

import unittest


class RomanNumeralKaantaja(object):
    def __init__(self):
        self.roman_dict = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        
        
    def convert_to_decimal(self, rom_num):
        val = 0
        for char in rom_num:
            val += self.roman_dict[char]
        return val
        
class RomanNumeralKaantajaTest(unittest.TestCase):
    def setUp(self):
        print "Luodaan instanssi romanNumeralKaantaja luokasta"
        self.cvt = RomanNumeralKaantaja()
        
    def tearDown(self):
        print "Tuhotaan luotu instanssi(tätä ei oikeesti nyt tarttisi koska instanssi alustetaan aina)"
        self.cvt = None
    
    def test_parsing_millenia(self):
        self.assertEquals(1000, self.cvt.convert_to_decimal("M"))
        
    def test_parsing_halfmillenia(self):
        self.assertEquals(500, self.cvt.convert_to_decimal("D"))
    
    def test_parsing_centuria(self):
        self.assertEquals(100, self.cvt.convert_to_decimal("C"), "Value is wrong")

    def test_parsing_halfcenturia(self):
        self.assertEquals(50, self.cvt.convert_to_decimal("L"))

    def test_parsing_kyba(self):
        self.assertEquals(10, self.cvt.convert_to_decimal("X"))
        
    def test_parsing_halfkyba(self):
        self.assertEquals(5, self.cvt.convert_to_decimal("V"))
        
    def test_parsing_yks(self):
        self.assertEquals(1, self.cvt.convert_to_decimal("I"))
        
    def test_empty_roman_number(self):
        self.assertTrue(self.cvt.convert_to_decimal("") == 0)
        self.assertFalse(self.cvt.convert_to_decimal("") > 0)
        
    def test_no_number(self):
        self.assertRaises(TypeError, self.cvt.convert_to_decimal, None)
 
if __name__ == "__main__":
    unittest.main()