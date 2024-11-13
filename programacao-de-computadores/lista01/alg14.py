########################################
#Programa: alg14.py || lista01
# Autor: Raissa Cavalcanti
# Descrição: Média disciplina
########################################

# Considerando todas as notas diferentes

primeira_disciplina = float(input("Qual a sua nota na primeira disciplina? \n"))
segunda_disciplina = float(input("Qual a sua nota na segunda disciplina? \n"))
terceira_disciplina = float(input("Qual a sua nota na terceira disciplina? \n"))

media = ((primeira_disciplina + segunda_disciplina + terceira_disciplina) / 3)

if (media < 5): 
    if (primeira_disciplina < segunda_disciplina and primeira_disciplina < terceira_disciplina):
        print("Sugiro que você abandone sua Primeira disciplina, pois sua nota está muito baixa.")
    elif (segunda_disciplina < primeira_disciplina and segunda_disciplina < terceira_disciplina):
        print("Sugiro que você abandone a sua Segunda disciplina, pois sua média está muito baixa.")
    else:
       print("Sugiro que você abandone a sua Terceira disciplina, pois a sua média está muito baixa")
elif (media >= 5 and media <7): 
    if (primeira_disciplina < segunda_disciplina and primeira_disciplina < terceira_disciplina):
        print("Sugiro que você tome cuidado com a sua Primeira disciplina, pois sua nota está muito baixa.")
    elif (segunda_disciplina < primeira_disciplina and segunda_disciplina < terceira_disciplina):
        print("Sugiro que você tome cuidado com a sua Segunda disciplina, pois sua média está muito baixa.")
    else:
       print("Sugiro que você tome cuidado com a sua Terceira disciplina, pois a sua média está muito baixa")
else:
    print("As suas notas estão boas, continue assim!")           
