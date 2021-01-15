while True:
    print('-'*30)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))

    if tabuada < 0:
        break

    print('-'*30)
    for i in range(0, 10):
        print(f'{tabuada} x {i + 1:3} = {tabuada * (i + 1):3}')
    
