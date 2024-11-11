import random

count = 0
pensando = random.randint(1, 5)

resp = int(input('Advinhe o número que estou pensando de 1 a 10: '))

while resp != pensando:
    resp = int(input('Advinhe novamente o número: '))
    count += 1

print(f'O número em que eu pensei era {pensando}\nVocê acertou em {count} palpite(s)')



