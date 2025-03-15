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
    
print("Resultado da função moda(): ", moda(dados3))    

print("Resultado da função interna: ", mode(dados3)) 

print(50 * "-")

print("Média Ponderada:")

dados4 = np.array([10, 11, 12, 13, 14, 15, 15, 17, 20, 25])  # Array do tipo Numpy
pesos = np.array([2, 3, 4, 2, 3, 5, 4, 2, 4, 5])  # Array do tipo Numpy

def media_ponderada(valor1, valor2):                                     # Função do cálculo da Média Ponderada
    if len(valor1) != len(valor2):                                            # Testa se quantidades são diferentes 
        return 'Quantidades de elemetos diferentes entre dados4 e Pesos.'     # Retorna Mensagem caso haja diferença
    else:
        zipado = zip(valor1, valor2)                                          # Iterador de Tuplas
        multiplicado = [x * y for x, y in zipado]                             # Multiplica Valor1 e Valor2
        a = np.sum(multiplicado)                                              # Soma valores multiplicados
        b = np.sum(valor2)                                                    # Soma Pesos
        media_ponderada = a / b                                               # Calcula Média Ponderada
        media_ponderada = media_ponderada.round(2)                            # # Arredonda a valor
        return media_ponderada                                                # Retorna Média Ponderada
    

print("Resultado da função media_ponderada(): ", media_ponderada(dados4, pesos))         # Chamada da função com Array(dados4) 

print("Resultado da função interna: ", np.average(dados4, weights=pesos).round(2))         # Função interna do Numpy para comparação dos valores

print(50 * "-")

print("Média Geométrica:")

dados5 = np.array([2, 8, 32]) 

def media_geometrica(valor):                                  # Função do cálculo da Média Ponderada
    quantidade  = len(valor)                                       # Quantidade de elementos do Array 
    valor_multip = np.prod(valor) ** (1 / quantidade)
    media_geometrica = math.ceil(valor_multip)
    return media_geometrica

print("Resultado da função media_geometrica(): ", media_geometrica(dados5) )

print("Resultado da função interna: ", np.prod(dados5) ** (1/3))