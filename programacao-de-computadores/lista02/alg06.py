########################################
#Programa: alg06.py || lista02
# Autor: Raissa Cavalcanti
# Descrição: Soma Sucessiva
########################################

primeiro_valor = int(input("Digite o Primeiro valor:\n"))
segundo_valor = int(input("Digite o Segundo Valor: \n"))
soma = primeiro_valor
i = 1

while (i<=segundo_valor):
    print(f"{primeiro_valor} x {i} = {soma}")
    soma += primeiro_valor
    i = i+ 1 