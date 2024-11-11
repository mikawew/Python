soma = count = media = maior = menor = 0
resp = 'S'


while resp in 'Ss':
    n1 = int(input('Digite um número: '))
    count += 1

    soma += n1

    if count == 1:
        maior = menor = n1

    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / count
print(f'Voce digitou {count} e a média foi {media}')
print(f'O maior valor foi {maior} e o menos foi {menor}')

