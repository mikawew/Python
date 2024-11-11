from time import sleep

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

resp = 0

while resp != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')

    resp = int(input('O que deseja fazer com os dois números? '))

    if resp == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} deu {soma}')

    elif resp == 2:
        multi = n1 * n2
        print(f'A multiplicação entre {n1} * {n2} deu {multi}')

    elif resp == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')

    elif resp == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro novo número: '))

    elif resp == 5:
        print('Finalizando...')
        sleep(2)

    else:
        print('Opção Inválida!')
print('Você saiu do programa!')
