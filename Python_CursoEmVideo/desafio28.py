import random

sua_resp = int(input('Advinhe meu número de 1 a 5: '))

pc_resp = random.randint(1, 5)

if sua_resp == pc_resp:
    print('PARABÉNS, você acertou o número')
else:
    print(f'Você errou, o número que eu pensei era {pc_resp} e o seu era {sua_resp}')

print('Jogue novamente...')




