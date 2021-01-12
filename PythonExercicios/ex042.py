print('Vou te perguntar o comprimento de 3 retas e dizer se é possível formar um triângulo')

reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda reta: '))
reta3 = int(input('Digite a terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Você pode formar um triângulo')
    if reta1 == reta2 == reta3:
        print('Você tem um triângulo equilátero, pois todos os lados são iguais')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('Você tem um triângulo isósceles, pois dois lados são iguais')
    else: 
        print('Você tem um triângulo escaleno, pois todos os lados são diferentes')
else:
    print('Você não pode formar um triângulo')
