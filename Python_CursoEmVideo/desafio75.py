guarda = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))

print(f'Você digitou os valores: {guarda}')
print(f'O valor 9 apareceu {guarda.count(9)} vezes.')
if 3 in guarda:
    print(f'O valor 3 apareceu na {guarda.index(3) + 1}º posição.')
else:
    print('O valor 3 não foi digitado nenhuma vez.')
for c in guarda:
    if c % 2 == 0:
        print(c, end=' ')


