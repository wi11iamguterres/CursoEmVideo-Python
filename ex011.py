largura=float(input('Insira a largura da parede (em metros): '))
altura=float(input('Insira a altura da parede (em metros): '))
area=largura*altura
tinta=area/2

print('A área da parede é: {:.2f}m². Será necessário {:.2f}L de tinta para pinta-lá.'.format(area,tinta))