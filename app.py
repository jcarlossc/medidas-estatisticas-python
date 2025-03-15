import pandas as pd 
import numpy as np
from statistics import mode
import math

print("""
MEDIDAS ARITMÉTICAS
Medidas de Tendência Central:
""")

print("* Média Aritmética:")

dados1 = np.array([10, 10, 10, 11, 12, 13, 14, 15, 15, 17, 20, 25])  # Array do tipo Numpy

def media_aritmetica(lista):                 # Função de cálculo da Média Aritmética
    if len(lista) == 0:                            # Testa se array está vazio
        return 'O Array está vazio.'               # Caso quantidade igual a zero, retorna mensagem
    elif len(lista) == 1:                          # Testa se quantidade de elementos do Array é igual a um
        return lista[0]                            # Caso quantidade igual a um, retorna lista do elemento
    else:
        soma_elementos = lista.sum()               # Soma dos elementos do Array
        quantidade = len(lista)                    # Quantidade de elementos do Array
        media = soma_elementos / quantidade        # Calcula a média
        media = media.round(2)                     # Arredonda a valor para dois números de ponto flutuante
        return media                               # Retorna Média 
    
print("Resultado da função media_aritmetica(): ", media_aritmetica(dados1))       # Chamada da função com Array(dados1)     

print("Resultado da função interna: ", dados1.mean().round(2))         # Função interna do Numpy para comparação dos valores

print(50 * "-")

