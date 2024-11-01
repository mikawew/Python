frase = str(input('Digite uma frase: ').strip()).upper()

a_maiusc = frase.count('A')
print(f'O "a" aparece: {a_maiusc}')

print(f'A primeira letra A apareceu na posição: {frase.find('A') + 1}')

print(f'A última letra A apareceu na posição: {frase.rfind('A') + 1}')
