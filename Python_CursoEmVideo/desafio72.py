num = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte') # 0 a 19

while True:
    n1 = int(input('Digite um número de 0 a 20: '))
    if 0 <= n1 <= 20:
        break
    print('Tente Novamente. ', end='')
print(num[n1-1])

