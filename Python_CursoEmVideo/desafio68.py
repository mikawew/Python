from random import randint

soma = count = 0
pc_resp = randint(1,10)

while True:
    print('Vamos jogar PAR ou IMPAR!')
    jogador = int(input('Digite um valor: (de 1 a 10)'))
    soma = jogador + pc_resp
    tipo = ' '


    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc_resp}. Total de {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            count += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            count += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos Jogar Novamente!')
print(f'GAME OVER\nVocê venceu {count} vezes')


