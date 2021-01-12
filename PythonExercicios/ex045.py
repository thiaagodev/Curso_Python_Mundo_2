import random

print('Vamos jogar Jokenpô!')
jogada = int(input('Escolha entre Pedra(1), Papel(2) ou Tesoura(3): '))

jogadas = ['Pedra', 'Papel', 'Tesoura']
jogada_computador = random.choice(jogadas)


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
else: 
    print(f'Deu empate! você jogou {jogadas[jogada - 1]} e o computador jogou {jogada_computador}')

