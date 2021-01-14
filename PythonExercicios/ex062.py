a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termos = 10

while termos != 0:
    count = a
    while count < a + (termos * r):
        print(count, end=', ')
        count += r
    termos_a_mais = int(input('Quantos termos deseja mostrar a mais? '))
    if termos_a_mais == 0:
        termos = 0
    else:
        termos += termos_a_mais
