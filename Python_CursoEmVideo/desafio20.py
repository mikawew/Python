import random

nome = input('Digite o nome do aluno: ')
nome1 = input('Digite o nome do aluno: ')
nome2 = input('Digite o nome do aluno: ')
nome3 = input('Digite o nome do aluno: ')

table = [nome, nome1, nome2, nome3]
random.shuffle(table)

print(f'A ordem sorteada é {table}')
