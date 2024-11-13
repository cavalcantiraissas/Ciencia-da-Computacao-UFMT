########################################
#Programa: alg03.py || lista01
# Autor: Raissa Cavalcanti
# Descrição: Número Real - raiz e quadrado
########################################

import math 

numero = float(input("Digite um número:\n"))
print(f"Você escolheu o número: {numero}\n")

quadrado = (numero*numero)
print(f"Quadrado de {numero} = {quadrado}\n")

raiz = math.sqrt(numero)
print(f"Raiz de {numero} = {raiz}")