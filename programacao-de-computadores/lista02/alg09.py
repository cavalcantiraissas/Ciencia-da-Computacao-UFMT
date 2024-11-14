########################################
#Programa: alg09.py || lista02
# Autor: Raissa Cavalcanti
# Descrição: Sequencia + Média
########################################

i = 1

referencia = int(input("Digite o valor de referência: "))

valor_1 = int(input("Digite o primeiro valor a ser somado: "))
valor_2 = int(input("Digite o segundo valor a ser somado: "))
valor_3 = int(input("Digite o terceiro valor a ser somado: "))

soma = (valor_1 + valor_3 + valor_2)

if (soma>referencia):
    while(i<=soma):
        print(i)
        i+=1
else:
     while(i<=referencia):
        print(i)
        i+=1   