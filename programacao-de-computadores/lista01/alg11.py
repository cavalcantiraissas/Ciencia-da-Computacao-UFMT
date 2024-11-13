########################################
#Programa: alg10.py || lista01
# Autor: Raissa Cavalcanti
# Descrição: Maior e Menor - 3 valores
########################################

primeiro_valor = int(input("Digite o Primeiro valor: \n"))
segundo_valor = int(input("Digite o Segundo valor: \n"))
terceiro_valor = int(input("Digite o Terceiro valor:\n"))

## Primeiro número maior
if (primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor): 
    print(f"{primeiro_valor} é maior que {segundo_valor} e {terceiro_valor}")
## Números iguais    
elif (primeiro_valor == segundo_valor and segundo_valor == terceiro_valor):
    print("Os três numeros são iguais")

## Segundo número maior
elif (segundo_valor > primeiro_valor and segundo_valor > terceiro_valor): 
    print(f"{segundo_valor} é maior que {primeiro_valor} e {terceiro_valor}")    

## Terceiro número é maior
else:
    print(f"{terceiro_valor} é maior que {primeiro_valor} e {segundo_valor}")    