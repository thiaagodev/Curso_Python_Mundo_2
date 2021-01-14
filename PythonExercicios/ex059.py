from time import sleep

escolha = -1

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro: '))

while escolha != 5:
    print('O que deseja fazer com esses números?')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    escolha = int(input('Sua escolha: '))

    if escolha == 1:
        print(f'O resultado é: {num1} + {num2} = {num1 + num2}')
    if escolha == 2:
        print(f'O resultado é: {num1} x {num2} = {num1 * num2}')
    if escolha == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        elif num2 > num1:
            print(f'{num2} é maior que {num1}')
        else:
            print('Os dois números são iguais')
    if escolha == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro: '))
    if escolha == 5:
        sair = input('Deseja finalizar o programa? [S / N]: ').upper()
        if sair == 'N':
            escolha = -1
    sleep(2)
