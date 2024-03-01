from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
print('O ângolo de {} tem o SENO de  {:.2f}'.format(angulo, seno))
coseno = cos(radians(angulo))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(angulo, coseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
