########################################
#Programa: alg12.py || lista01
# Autor: Raissa Cavalcanti
# Descrição: 3 Valores - meio
########################################

primeiro_valor = int(input("Digite o Primeiro valor: \n"))
segundo_valor = int(input("Digite o Segundo valor: \n"))
terceiro_valor = int(input("Digite o Terceiro valor:\n"))

## "A" como valor do meio
if ((segundo_valor > primeiro_valor and primeiro_valor > terceiro_valor) or (terceiro_valor > primeiro_valor and primeiro_valor > segundo_valor)) :
    print(f"{primeiro_valor} é o valor do meio entre {segundo_valor} e {terceiro_valor}")
elif ((primeiro_valor > segundo_valor and segundo_valor > terceiro_valor) or (terceiro_valor > segundo_valor and segundo_valor > primeiro_valor)): 
    print(f"{segundo_valor} é o valor do meio entre {primeiro_valor} e {terceiro_valor}")
else:
    print(f"{terceiro_valor} é o valor do meio entre {segundo_valor} e {primeiro_valor}")
    
