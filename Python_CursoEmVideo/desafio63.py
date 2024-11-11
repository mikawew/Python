n1 = int(input('Digite quantos números deseja mostrar pelo elemento da Fibonacci: '))

c = 0
t2 = 0
cont = 3

print(f'{c} -> {t2}')
while cont <= n1:
    t3 = c + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')

