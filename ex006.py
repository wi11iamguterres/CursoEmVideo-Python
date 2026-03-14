import math

numero=int(input('Insira o número: '))
dobro=numero*2
triplo=numero*3
raiz=math.sqrt(numero)

print('O número inserido foi {}. Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.3f}.'.format(numero,dobro,triplo,raiz))
