from math import factorial

n1 = int(input('Digite um número: '))

print(f'O fatorial de {n1}! é:')

for c in range(n1, 0, -1):
    f = factorial(n1)
    if c != 1:
        print(c, end='x')
    else:
        print(c, end=' = ')
        print(f, end='')

