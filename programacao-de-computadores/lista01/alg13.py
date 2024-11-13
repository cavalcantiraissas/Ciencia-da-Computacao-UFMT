########################################
#Programa: alg13.py || lista01
# Autor: Raissa Cavalcanti
# Descrição: 2 valores - dobro
########################################

primeiro_numero = (int(input("Digite o primeiro valor: \n")))
segundo_numero = (int(input("Digite o segundo valor: \n")))

if (primeiro_numero > segundo_numero): 
    segundo_numero_2x = (segundo_numero * 2)
    if (segundo_numero_2x > primeiro_numero):
        print(f"Inicialmente, {primeiro_numero} era maior que {segundo_numero}\nMas, ao dobrar, {segundo_numero_2x} se torna maior que {primeiro_numero} ")
    else:
        print(f"Mesmo dobrando o valor de {segundo_numero} ({segundo_numero_2x}), ele ainda não é maior que {primeiro_numero}")
else:
    primeiro_numero_2x = (primeiro_numero *2)
    if (primeiro_numero_2x > segundo_numero):
        print(f"Inicialmente, {segundo_numero} era maior que {segundo_numero}\nMas, ao dobrar, {primeiro_numero} se torna maior que {segundo_numero} ")         
    else: 
         print(f"Mesmo dobrando o valor de {primeiro_numero} ({primeiro_numero_2x}), ele ainda não é maior que {segundo_numero}")
