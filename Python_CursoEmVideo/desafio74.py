from random import randint

tupla = (randint(1,5), randint(1,5), randint(1,5), randint(1,5), randint(1,5))

print('Os valores sorteados: ', end='')

for c in tupla:
    print(f'{c}', end=' ')

print(f'\nO maior valor foi: {max(tupla)}')
print(f'O menor valor foi: {min(tupla)}')


