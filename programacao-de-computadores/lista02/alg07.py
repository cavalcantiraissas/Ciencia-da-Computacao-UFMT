########################################
#Programa: alg07.py || lista02
# Autor: Raissa Cavalcanti
# Descrição: Tabuada
########################################

numero = int(input("Tabuada do número: "))

i = 1
resultado = numero

while (i<=10):
    print(f"{numero} x {i} = {resultado}")
    resultado += numero
    i +=1