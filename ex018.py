import math

ang=float(input("Informe o ângulo a ser calculado o seno, o cosseno e tangente: "))
ang=math.radians(ang)
cosseno=math.cos(ang)
seno=math.sin(ang)
tangente=math.tan(ang)

print("O ângulo {}° possui cosseno de {:.3f}°, seno de {:.3f}° e tangente de {:.3f}°.".format(ang,cosseno, seno, tangente))