s = 0
count = 0
for c in range (1, 500, 2):
    print(c)
    if c % 3 == 0:
        s += c
        count += 1

print(f'A soma de todos os {count} ímpares e múltiplos de 3 é: {s}')

