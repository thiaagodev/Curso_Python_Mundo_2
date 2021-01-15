from random import randint
from time import sleep

vitorias = jogada_player = jogada_pc = soma = 0
print('Vamos jogar par ou ímpar!')

while True:
    player = int(input('Par[0] ou ímpar[1]? '))
    jogada_pc = randint(1, 10)

    if player == 0:
        print('Ok! eu escolho ímpar!')
        sleep(1)   
    if player == 1:
        print('Ok! eu escolho par!')
        sleep(1)
    
    jogada_player = int(input('Digite um número: '))   
    soma = jogada_player + jogada_pc

    if player == 0 and soma % 2 == 0:
        vitorias += 1
    elif player == 1 and soma % 2 != 0:
        vitorias += 1
    else:
        print(f'Você perdeu! você jogou {jogada_player} e o computador {jogada_pc}, a soma vale {soma}')
        break

sleep(0.5)
print(f'Você teve {vitorias} vitórias consecutivas')
