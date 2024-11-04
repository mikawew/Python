n1 = int(input('Digite o primeiro valor para formar um triangulo: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if (n1 + n2) > n3 and (n2 + n3) > n1 and (n3 + n1) > n2:
     print('É possível criar um triângulo com esses resultados')
else:
    print()
    print('Não é possível criar um triângulo com isso.')

print()
print('Digite de novo...')

