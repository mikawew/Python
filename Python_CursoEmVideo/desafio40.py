n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f'PARABÉNS você está APROVADO com {media:.2f} na média')

elif 5 <= media <= 6.9:
    print(f'VOCÊ está de RECUPERAÇÃO! SUA média {media}')

else:
    print(f'INFELIZMENTE você está REPROVADO! VOCÊ tirou média {media}')
