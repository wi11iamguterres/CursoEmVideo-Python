salario=float(input('Insira o valor do salário: '))
sal_mais_15=(salario+(salario*0.15))

print('O valor do salário é: R${:.2f}. \nO valor do salário com aumento de 15% é: R${:.2f}'.format(salario, sal_mais_15))