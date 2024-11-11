from math import factorial

n1 = int(input('Digite um número: '))
f = factorial(n1)

print(f'O fatorial de {n1}! é:')

while n1 != 1:
    print(n1, end='x')
    n1 -= 1
    if n1 == 1:
        print(n1, end=' = ')
        print(f, end='')






