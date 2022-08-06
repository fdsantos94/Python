# Somando dois numeros e retornando ao usuário com algumas formas diferentes
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2

# Print convencional
print('A soma dos valores é:', soma)
print('A soma entre:', n1, 'e', n2, 'vale:', soma)

# Print usando Python 3
print('A soma dos valores é: {}'.format(soma))
print('A soma entre {} e {} vale: {}'.format(n1, n2, soma))
