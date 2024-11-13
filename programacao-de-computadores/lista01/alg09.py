########################################
#Programa: alg08.py || lista01
# Autor: Raissa Cavalcanti
# Descrição: Divisível: 2,3,5,10
########################################

numero = int(input("Digite um número:\n"))

div_2 = numero%2
div_3 = numero%3
div_5 = numero%5
div_10 = numero%10

if (div_2 == 0 and div_3 == 0 and div_10 == 0 ): 
    print(f"{numero} é divisível por 2, 3 e 10")  
elif (div_3 == 0 and div_5 == 0 and div_10 == 10): 
    print(f"{numero} é divisível por 3, 5 e por 10")     
elif (div_2 == 0 and div_10 == 0 ): 
    print(f"{numero} é divisível por 2 e por 10")
elif (div_5 == 0 and div_10 == 0 ): 
    print(f"{numero} é divisível por 5 e por 10")
elif (div_2 == 0 and div_3 == 0 ): 
    print(f"{numero} é divisível por 2 e por 3")
elif (div_3 == 0 and div_5 == 0 ): 
    print(f"{numero} é divisível por 3 e por 5") 
elif (div_2 == 0): 
    print(f"{numero} é divisível por 2")
elif (div_3 == 0): 
    print(f"{numero} é divisível por 3")
elif (div_5 == 0): 
    print(f"{numero} é divisível por 5")
elif (div_10 == 0): 
    print(f"{numero} é divisível por 10")   
else:
    print("O número escolhido não é divisível por 2, 3, 5 ou 10")        