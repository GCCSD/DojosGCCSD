#!/usr/bin/env python

__authors__ = (
    "Sigano",
    "InFog",
    "Paulo",
    "Coragem",
    "Kretcheu"
)

class ProdutoVetores():

    def produto(self, A, B):
        
        dimensao = A.__len__()
        resultado = 0  
        
        for i in range(dimensao):
            resultado += A[i] * B[i]
            
            
        return resultado
