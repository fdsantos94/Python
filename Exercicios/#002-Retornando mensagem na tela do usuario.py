# Retornando mensagem de boas vindas ao usuário

# Forma 1
nome = input('Digite seu nome: ')
retorno = 'É um prazer te conhecer,'
print(retorno, nome + '!')

# Forma 2
nome = input('Digite seu nome: ')
retorno = 'É um prazer te conhecer,'
print(retorno, '{}!'.format(nome))

# Forma 2 com mais de uma variavel
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
retorno = 'É um prazer te conhecer,'
print(retorno, '{} {}!'.format(nome, sobrenome))
