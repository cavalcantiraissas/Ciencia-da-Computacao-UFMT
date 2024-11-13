########################################
#Programa: alg06.py || lista01
# Autor: Raissa Cavalcanti
# Descrição: Número real: raiz ou quadrado
########################################

import math

numero = float(input("Digite um número: \n"))

if (numero >=0):
    raiz = (math.sqrt(numero))
    print(f"Raiz quadrada de {numero} = {raiz}")
else:
    quadrado = (numero * numero)
    print(f"Quadrado de {numero} = {quadrado}")    