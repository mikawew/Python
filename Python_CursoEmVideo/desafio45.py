import random

print(''' Vamos jogar Pedra, Papel e Tesoura
[1] Pedra
[2] Papel
[3] Tesoura''')

jogadas = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0, 2)

print(f'O computador escolher {jogadas[computador]}')

jogador = int(input('Qual a sua jogada? '))

print()
print(f'Jogador jogou {jogadas[jogador]}')
print(f'Máquina jogou {jogadas[computador]}')
print()

if computador == 0: # PEDRA
    if jogador == 0:
        print('Houve um EMPATE')

    elif jogador == 1:
        print('O humano VENCEU! ')

    elif jogador == 2:
        print('A máquina VENCE!')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: # Papel
    if jogador == 0:
        print('A máquina VENCE!')

    elif jogador == 1:
        print('Houve um EMPATE!')

    elif jogador == 2:
        print('O humano VENCE!')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: # Tesoura
    if jogador == 0:
        print('O humano VENCE!')

    elif jogador == 1:
        print('A máquina VENCE!')

    elif jogador == 2:
        print('Houve um EMPATE')

    else:
        print('JOGADA INVÁLIDA')

