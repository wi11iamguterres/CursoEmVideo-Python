preco=float(input('Insira o valor do produto: '))
preco_desc=(preco-(preco*0.05))
print('O valor do produto é: R${:.2f}.\nO valor com o desconto é: R${:.2f}'.format(preco,preco_desc))

