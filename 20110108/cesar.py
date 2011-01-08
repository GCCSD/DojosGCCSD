#!/usr/bin/env python

import string

class Cesar(object): 
    
    def __init__(self):
        self.INICIO = 65
        self.FIM = 90
        self.ESPACO = 32
    
    def crypt(self, entrada = "", chave = 0):
        saida = ""
        entrada = entrada.upper()

        for letra in entrada:
            valor = ord(letra)
            
            if (not valor == self.ESPACO):
                valor += chave
                if (valor > self.FIM):
                    valor -= 26
            saida += chr(valor)
            
        return saida
    
    def decrypt(self, entrada = "", chave = 0):
        saida = ""
        entrada = entrada.upper()
        
        for letra in entrada:
            valor = ord(letra)
            
            if (not valor == self.ESPACO):
                valor -= chave
                if (valor < self.INICIO):
                    valor += 26
            saida += chr(valor)
        
        return saida
