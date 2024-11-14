########################################
#Programa: alg10.py || lista02
# Autor: Raissa Cavalcanti
# Descrição: Sequencia + Média
########################################

i = 1
numero_novo = 0 

numero = int(input("Digite um valor: "))

while ( i<=numero):
    if (i %3==0 or i == 1):
        numero_novo = (i*2)
        print(numero_novo)
    else:
        numero_novo = (i/2)
        print(numero_novo)
    i+=1        
