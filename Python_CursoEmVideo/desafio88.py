from random import randint
from time import sleep
lista = list()
jogos = list()

total = 1

quant_jogos = int(input('Quanto jogos da MEGA SENA você deseja? '))

while total <= quant_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('=' * 30, f'SORTEANDO {total-1} JOGOS', '=' * 30)
for i, l in enumerate(jogos):
    print(f'Jogos {i+1}: {l}')
    sleep(1)
print('BOA SORTE!!')
