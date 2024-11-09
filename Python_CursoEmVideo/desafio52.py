n1 = int(input('Digite um número: '))
tot = 0

for c in range (1, n1 + 1):
    if n1 % c == 0:
        tot += 1
        print('\033[34m', end='')
    else:
        print('\033[31m', end='')
    print(f'{c} ',end='')

print(f'\nO número {n1} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')
