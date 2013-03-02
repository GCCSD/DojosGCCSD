#!/usr/bin/env python

__authors__ = [
    "bralpassos",
    "Ferauche",
    "lerox",
    "InFog",
    "mathop"
]

import unittest

from palavrasprimas import palavraPrima

class TestPalavrasprimas(unittest.TestCase):

    def testeNaoPrimo(self):
        resultado = palavraPrima('abc') # 6
        self.assertEqual(resultado, False)
        
        resultado = palavraPrima('def') # 15
        self.assertEqual(resultado, False)
        
        resultado = palavraPrima('ac') # 4
        self.assertEqual(resultado, False)
        
        resultado = palavraPrima('bbaa') # 6
        self.assertEqual(resultado, False)
    
        resultado = palavraPrima('abAB') #1 + 2 + 27 + 28 = 58
        self.assertEqual(resultado, False)
        
    
    def testePrimo(self):
        resultado = palavraPrima('ABCA') # 27 + 28 + 29 + 27 = 111
        self.assertEqual(resultado, True)
        
        resultado = palavraPrima('aa') #2
        self.assertEqual(resultado, True)
        
        resultado = palavraPrima('ab') #3
        self.assertEqual(resultado, True)
        

if __name__ == "__main__":
    unittest.main()
