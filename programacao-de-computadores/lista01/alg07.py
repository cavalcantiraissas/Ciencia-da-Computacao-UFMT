########################################
#Programa: alg07.py || lista01
# Autor: Raissa Cavalcanti
# Descrição: Impressão de Cores
########################################

numero = int(input("Digite um número: "))

if (numero < 0 ): 
    print("Branco")
elif (numero >= 0 and numero<=100): 
    print("Verde")  
elif (numero>100 and numero<=1000):
    print("Azul")
else:
    print("Vermelho")          