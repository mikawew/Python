peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('O seu IMC está ABAIXO DO PESO')

elif 18.5 >= imc <= 25:
    print('O seu IMC está no PESO IDEAL')

elif 25 < imc <= 30:
    print('O seu IMC está em SOBREPESO')

elif 30 > imc <= 40:
    print('O seu IMC está em OBESIDADE')

else:
    print('O seu IMC está em OBESIDADE MÓRBIDA')
