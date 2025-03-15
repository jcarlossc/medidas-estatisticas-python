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

def media_aritmetica(valor):                 # Função de cálculo da Média Aritmética
    if len(valor) == 0:                            # Testa se array está vazio
        return 'O Array está vazio.'               # Caso quantidade igual a zero, retorna mensagem
    elif len(valor) == 1:                          # Testa se quantidade de elementos do Array é igual a um
        return valor[0]                            # Caso quantidade igual a um, retorna valor do elemento
    else:
        soma_elementos = valor.sum()               # Soma dos elementos do Array
        quantidade = len(valor)                    # Quantidade de elementos do Array
        media = soma_elementos / quantidade        # Calcula a média
        media = media.round(2)                     # Arredonda a valor para dois números de ponto flutuante
        return media                               # Retorna Média 
    
print("Resultado da função media_aritmetica(): ", media_aritmetica(dados1))       # Chamada da função com Array(dados1)     

print("Resultado da função interna: ", dados1.mean().round(2))         # Função interna do Numpy para comparação dos valores

print(50 * "-")

print("* Mediana:")

dados2 = np.array([25, 13, 9, 11, 20, 15, 12, 21])  # Array do tipo Numpy

def mediana(valor):                          # Função de cálculo da Mediana
    valor = np.sort(valor)                         # Ordenação do Array(a Mediana precisa de ordem)
    if len(valor) == 0:                            # Testa se quantidade de elementos é igual a zero
        return 'O Array está vazio.'               # Caso quantidade igual a zero, retorna mensagem
    elif len(valor) == 1:                          # Testa se quantidade de elementos do Array é igual a um
        return valor[0]                            # Caso quantidade igual a um, retorna valor do elemento
    else:
        if len(valor) % 2 == 0:                    # Testa se quantidade de elementos de Array é Par, caso seja...
            a = (len(valor) // 2) - 1              # Obtem a divisão da quantidade de elementos do Array menos um
            b = len(valor) // 2                    # Obtem a divisão da quantidade de elementos do Array
            mediana = (valor[a] + valor[b]) / 2    # Soma e divide os respectivos valores
            mediana = mediana.round(2)             # Arredonda a valor para dois números de ponto flutuante 
            return mediana                         # Retorna Mediana
        else:                                      # Caso a uantidade de elementos de Array seja Impar
            a = (len(valor) // 2)                  # Obtem a divisão da quantidade de elementos do Array
            mediana = valor[a]                     # Obtem Mediana
            return mediana                         # Retorna Mediana
        

print("Resultado da função mediana(): ", mediana(dados2))        # Chamada da função com Array(dados2) 

print("Resultado da função interna: ", np.median(dados2).round(2))         # Função interna do Numpy para comparação dos valores

print(50 * "-")

print("* Moda:")

dados3 = np.array([25, 13, 9, 11, 13, 20, 15, 12, 21, 25, 25])  # Array do tipo Numpy

def moda(valor):                               # Função do cálculo da Moda
    if len(valor) == 0:                              # Testa se Array está vazio
        return 'O Array está vazio.'                 # Retorna Mensagem, caso vazio
    elif len(valor) == 1:                            # Testa se Array contem um elemento
        return valor[0]                              # Retorna elemento
    else:
        serie = pd.Series(valor)                     # Cria uma série Pandas
        serie = serie.value_counts()                 # Conta as quantidades de elementos
        moda = serie.index[0]                        # Obtem o elemento de maior frequência
        return moda                                  # Retorna Moda
    
print("Resultado da função moda(): ", moda(dados3) )    

print("Resultado da função interna: ", mode(dados3)  ) 

print(50 * "-")