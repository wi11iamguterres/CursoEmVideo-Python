import random
try:
    aluno1=input("Informe o nome do primeiro aluno: ")
#1 == aluno1
    aluno2=input("Informe o nome do segundo aluno: ")
#2 == aluno2
    aluno3=input("Informe o nome do terceiro aluno: ")
#3 == aluno3
    aluno4=input("Informe o nome do quarto aluno: ")
#4== aluno4

    lista=[aluno1, aluno2, aluno3, aluno4]
except:
    print(lista)

sorteado=random.choice(lista)
print("O aluno escolhido foi: {}.".format(sorteado))

'''if sorteado == 1:
    print(aluno1)
if sorteado == 2:
    print(aluno2)
if sorteado == 3:
    print(aluno3)
if sorteado == 4:
    print(aluno4)'''

