print('Gerador de PA')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('FIM')
    mais = int(input('Quantos temos você quer mostrar a mais? '))
print(f'Foram finalizadas com {total} termos mostrados')
print('FIM')
