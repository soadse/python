while True:
    print('-'*33)
    num = int(input('Quer ver a \033[34mTABUADA\033[m de qual valor? '))
    print('-'*33)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
print('\033[31mPROGRAMA DE TABUADA ENCERRADO\033[m.\nVolte sempre😊!')
