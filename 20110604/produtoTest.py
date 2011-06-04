#!/usr/bin/env python

__authors__ = (
    "Sigano",
    "InFog",
    "Paulo",
    "Coragem",
    "Kretcheu"
)

import unittest

from produtoVetores import ProdutoVetores

class testeVetor(unittest.TestCase):
    def testeUmUm(self):
        vetor = ProdutoVetores()
        
        A = [1]
        B = [1]
        
        Resultado = 1
    
        self.assertEqual(Resultado, vetor.produto(A, B))
    
    def testeUmDois(self):
        vetor = ProdutoVetores()
        
        A = [1]
        B = [2]
        
        Resultado = 2
        
        self.assertEqual(Resultado, vetor.produto(A, B))
        
    def testeUmDoisUmDois(self):
        vetor = ProdutoVetores()
        
        A = [1,2]
        B = [1,2]
        
        Resultado = 5
        
        self.assertEqual(Resultado, vetor.produto(A,B))
     
    def testeTresTres(self):
        vetor = ProdutoVetores()
        
        A = [5, 6, 7]
        B = [1, 3, 4]
        
        Resultado = 51
        
        self.assertEqual(Resultado, vetor.produto(A, B))

if __name__ == '__main__':
    unittest.main()
