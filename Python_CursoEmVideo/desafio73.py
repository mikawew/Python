#16/11/2024
brasileirao_2024 = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Internacional', 'São Paulo', 'Cruzeiro', 'Bahia', 'Vasco da Gama', 'Atlético-Mineiro', 'Corinthians', 'Grêmio', 'EC Vitória', 'Chapecoense' ,'Atletico Paranaense', 'Fluminense', 'Criciúma', 'Juventude', 'Bragantino', 'Cuiabá', 'Atlético Clube Goianiense' ) # 0 a 20



for count, time in enumerate(brasileirao_2024[:5]):
    print(f'Os 5 primeiros colocados são: {time} em {count+1}º')

print()

for count, time in enumerate(brasileirao_2024[16:]):
    print(f'Os últimos 4 colocados são: {time} em {count+17}º')

print()

print(f'Uma lista com os times em ordem alfabética: {sorted(brasileirao_2024)}')

print(f'A Chapencoense está na posição: {brasileirao_2024.index("Chapecoense") + 1}º')

