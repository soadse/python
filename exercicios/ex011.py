l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, area))
print('Para pintar essa parede, você precisará de {}l de tintas'.format(tinta))

while True:
    s = 's'
    n = 'n'
    res = input('Deseja continuar? (s/n) ')
    if res == s:
        l = float(input('Largura da parede: '))
        a = float(input('Altura da parede: '))
        area = l * a
        tinta = area / 2
        print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, area))
        print('Para pintar essa parede, você precisará de {}l de tintas'.format(tinta))
    else:
        break