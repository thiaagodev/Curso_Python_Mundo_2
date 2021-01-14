a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
count = a

"""for i in range(a, a + (10 * r), r):
    print(i, end=', ')
"""
while count < a + (10 * r):
    print(count, end=', ')
    count += r
