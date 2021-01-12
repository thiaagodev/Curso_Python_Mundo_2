import random
from time import sleep

repetir = 1

print('Vamos jogar Jokenpô!')

while repetir == 1:
    jogada = int(input('Qual a sua jogada? Pedra[1], Papel[2] ou Tesoura[3]: '))

    jogadas = ['Pedra', 'Papel', 'Tesoura']
    jogada_computador = random.choice(jogadas)

    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!')
    sleep(0.5)

    print('-='*30)

    if jogada == 1 and jogada_computador == 'Tesoura':
        print(f'Você ganhou! você jogou pedra e o computador jogou {jogada_computador.lower()}')
    elif jogada == 1 and jogada_computador == 'Papel':
        print(f'Você perdeu! você jogou pedra e o computador jogou {jogada_computador.lower()}')
    elif jogada == 2 and jogada_computador == 'Pedra':
        print(f'Você ganhou! você jogou papel e o computador jogou {jogada_computador.lower()}')
    elif jogada == 2 and jogada_computador == 'Tesoura':
        print(f'Você perdeu! você jogou papel e o computador jogou {jogada_computador.lower()}')
    elif jogada == 3 and jogada_computador == 'Papel':
        print(f'Você ganhou! você jogou tesoura e o computador jogou {jogada_computador.lower()}')
    elif jogada == 3 and jogada_computador == 'Pedra': 
        print(f'Você perdeu! você jogou tesoura e o computador jogou {jogada_computador.lower()}')
    elif jogada != 1 and jogada !=2 and jogada != 3:
        print('Opção inválida! Tente novamente')
    else: 
        print(f'Deu empate! você jogou {jogadas[jogada - 1]} e o computador jogou {jogada_computador}')

    print('-='*30)

    repetir = int(input('Quer jogar denovo? SIM[1] | NÃO[0]: '))
