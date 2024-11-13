########################################
#Programa: alg10.py || lista01
# Autor: Raissa Cavalcanti
# Descrição: Maior e Menor
########################################

primeiro_valor = int(input("Digite o Primeiro valor: \n"))
segundo_valor = int(input("Digite o Segundo valor: \n"))

if (primeiro_valor > segundo_valor): 
    print(f"{primeiro_valor} é maior que {segundo_valor}")
elif (primeiro_valor == segundo_valor):
    print(f"{primeiro_valor} é igual a {segundo_valor}")

else:
    print(f"{segundo_valor} é maior que {primeiro_valor}")    