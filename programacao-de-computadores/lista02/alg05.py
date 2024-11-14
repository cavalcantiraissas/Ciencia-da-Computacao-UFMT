########################################
#Programa: alg05.py || lista02
# Autor: Raissa Cavalcanti
# Descrição: Limite + Incremento
########################################

limite = int(input("Digite um Valor Limite:\n"))
incremento = int(input("Digite o Valor de Incremento:"))
i = 0

if (limite>incremento):
    while(i<limite):
        print(i)
        i+=incremento

elif (limite<incremento):
    print("Incremento maior que limite. Tente novamente")