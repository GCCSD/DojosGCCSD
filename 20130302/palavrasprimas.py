#!/usr/bin/env python

def ehPrimo(num):
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, (num / 2) + 1, 2):
        if num % i == 0:
            return False
    
    return True

def palavraPrima(palavra):
    soma = 0
    
    for x in range(0, len(palavra)):
        codigo_ascii = ord(palavra[x])
        if 65 <= codigo_ascii <= 90:
            soma += codigo_ascii - 64
        else:
            soma += codigo_ascii - 96
        
    return ehPrimo(soma)

palavraPrima('abc')
