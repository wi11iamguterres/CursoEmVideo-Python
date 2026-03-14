import math
catOp=float(input("Informe o valor do cateto oposto: "))
catAdj=float(input("Informe o cateto adjacente: "))
hip=math.hypot(catOp,catAdj)

print("O triângulo retângulo com cateto oposto {}, com cateto adjacente {} tem a hipotenusa {}.".format(catOp, catAdj, hip))