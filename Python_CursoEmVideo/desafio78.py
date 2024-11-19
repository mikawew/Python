valores = list()

for c in range(0, 5):
    valores.append(int(input(f'Digite alguns números na {c+1}º posição: ')))

print(f'\nO maior valor da sua lista é {max(valores)}')
print(f'O menor valor da sua lista é {min(valores)}')

for v, valor in enumerate(valores):
    print(f'Na {v+1}º posição aparece: {valor}')

print(valores, end='')


