nome = str(input('Digite o seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())

print(len(nome) - nome.count(' '))

#print(nome.find(' '))

PrimeiroNome = nome.split()
print(len(PrimeiroNome[0]))

