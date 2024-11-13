########################################
#Programa: alg08.py || lista01
# Autor: Raissa Cavalcanti
# Descrição: Par ou Ímpar
########################################

numero = int(input("Digite um número: "))

par = numero % 2

if (par == 0): 
    print(f"{numero} = par")
else:
    print(f"{numero} = impar")
