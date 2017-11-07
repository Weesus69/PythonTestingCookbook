# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:00:14 2017

@author: Iso Wee
"""
import random
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class somaa():
    def __init__(self, nimi):
        self.nimi = nimi
        
    def tulosta_sata(self):
        for x in range(0,100):
            print x
            
    def monta_lukuu(self, montako):
        luvut = ""
        for x in range(0,montako):
            luvut += " " + str(x)
        return luvut
            
    def heippa(self):
        print "terppa %s" % self.nimi
    
    def summaa(self, luku):
        luku += 17
        return luku
 
#Tässä luokassa käpistellään webbia, jos haluttaisiin ajaa testejä niin kts. esim
# chrome_webbi_testi.py        
class webbi():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "http://www.python.org"
    
    def open_web_page(self):
        driver = self.driver
        driver.get(self.url)
        driver.maximize_window()
    
    def lopeta(self):
        driver = self.driver
        time.sleep(10)
        driver.close()



        
#Luodaan instanssi 'jorma' joka alustetaan kaikella sillä mikä on määritelty
#luokan __init__ metodissa eli tässä tapauksessa nimi
jorma = somaa('jorma')
jorma.tulosta_sata()
jorma.heippa()
print jorma.summaa(13)
print jorma.monta_lukuu(7)
print random.randint(1, 77)


f2 = open("luokka.txt", "w+")
f2.write("fhohweifwoefh")
f2.write(jorma.monta_lukuu(8))
f2.close()   

#testing weebi luokkaa
testi = webbi()
testi.open_web_page()
testi.lopeta()
