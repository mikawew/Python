num = [2, 5, 9, 1]

num.append(5)
num.sort(reverse=True)

for c, v in enumerate(num):
    print(f'Na posição {c+1}º de trás para frente tem os valores: {v}')


