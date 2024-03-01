num = int(input('Digite o valor em metros: '))
mm = num * 1000
cm = num * 100
dc = num * 10
m = num * 1
dam = num * 10
hm = num * 100
km = num * 1000
print('O valor é {} metros!\nE suas medidas são:\n{} mm\n{} cm\n{} dc\n{} m\n{} dam\n{} hm\n{} km.'
      .format(num, mm, cm, dc, m, dam, hm, km))
