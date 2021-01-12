valor = 0

for i in range(0, 500):
    if (i + 1) % 2 != 0 and (i + 1) % 3 == 0:
        valor += i + 1

print(valor)
