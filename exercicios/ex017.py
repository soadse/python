import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotensa vai medir {:.2f}'.format(hi))

'''cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenuza = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenuza))'''
