import random
from time import sleep

print('Vou pensar em um número entre 0 e 10, tente adivinhar!')
print('Estou pensando...')
sleep(2)

numero = random.randint(0, 10)
chute = -1
tentativas = 0

print('Pronto!')

while chute != numero:
    chute = int(input('Tente acertar o número: '))
    if chute > numero:
        print('Menos! Tente outra vez.')
    if chute < numero:
        print('Mais! Tente outra vez.')
    tentativas += 1

print(f'Parabéns! eu pensei em {numero} e você disse exatamente {chute} depois de {tentativas} tentativas.')
