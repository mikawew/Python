import random

nome = input('Digite o nome do 1 aluno: ')
nome1 = input('Digite o nome do 2 aluno: ')
nome2 = input('Digite o nome do 3 aluno: ')
nome3 = input('Digite o nome do 4 aluno: ')

table = [nome, nome1, nome2, nome3]

aleat = random.choice(table)

print(f'O aluno escolhido foi: {aleat}')



