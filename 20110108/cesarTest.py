#!/usr/bin/env python

import unittest
from cesar import Cesar

class CesarTest(unittest.TestCase):

    def testeABC(self):
        cesar = Cesar()
        entrada = "ABC"
        chave = 3
        valorEsperado = "DEF"

        self.assertEqual(valorEsperado, cesar.crypt(entrada, chave))
    
    def testeZ(self):
        cesar = Cesar()
        entrada = "Z"
        chave = 3
        valorEsperado = "C"

        self.assertEqual(valorEsperado, cesar.crypt(entrada, chave))

    def testeSPACE(self):
        cesar = Cesar()
        entrada = "A B C"
        chave = 3
        valorEsperado = "D E F"

        self.assertEqual(valorEsperado, cesar.crypt(entrada, chave))

    def testeDecriptDEF(self):
        cesar = Cesar()
        entrada = "D E F"
        chave = 3
        valorEsperado = "A B C"
        
        self.assertEqual(valorEsperado, cesar.decrypt(entrada, chave))

if __name__ == '__main__':
    unittest.main()
