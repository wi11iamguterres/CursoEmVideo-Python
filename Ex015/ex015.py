quilometros=float(input("Informe a quantidade de quilometros rodados com o carro: "))
dias=float(input("Informe a quantidade de dias utilizados pelo carro: "))

valor=(quilometros*0.15)+(dias*60)

print("O valor do aluguel do carro é de R${:.2f}.".format(valor))