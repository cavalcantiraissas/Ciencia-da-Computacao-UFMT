########################################
#Programa: alg08.py || lista02
# Autor: Raissa Cavalcanti
# Descrição: Sequencia + Média
########################################

i = 1
soma = 0

numeros = int(input("Quantos números serão lidos?: "))

while (i<=numeros):
    print(f"Digite o {i} valor: ")
    valor = int(input())
    soma += valor
    i+=1

media = (soma/numeros)
print(f"Média = {media}")       