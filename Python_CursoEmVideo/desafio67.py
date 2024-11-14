while True:
    n1 = int(input('Quer ver a tabuada de qual valor? '))
    if n1 < 0:
        break
    for c in range (1, 11):
        result_multi = n1 * c
        print(f'{n1} x {c} = {result_multi}')
print('Você digitou um número negativo!')

