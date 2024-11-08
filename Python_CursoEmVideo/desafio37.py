num = int(input('Digite um número inteiro: '))

print('''Conversões de número:
Escolha [1] para BINÁRIO
Escolha [2] para OCTAL
Escolha [3] para HEXADECIMAL''')

escolha = int(input('Escolha: '))

if escolha == 1:
    binario = bin(num)
    print(f'O número {num}, em BINARIO fica: {binario[2:]}')

elif escolha == 2:
    octal = oct(num)
    print(f'O número {num}, em OCTAL fica: {octal[2:]}')

else:
    hexadecimal = hex(num)
    print(f'O número {num}, em HEXADECIMAL fica: {hexadecimal[2:]}')

