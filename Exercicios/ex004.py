# Programa que ler algo e mostra na tela seu tipo primitivo e todas as informações possíveis
msg = input('Digite alguma coisa: ')

if msg.isnumeric():
    print('Você digitou um valor numérico com {} caracter'.format(len(msg)))
elif msg.isalpha():
    print('Você digitou um valor alfabético {} caracter'.format(len(msg)))
elif msg.isalnum():
    print('Você digitou um valor alfanumerico {} caracter'.format(len(msg)))

# print('O que você digitou é: {}'.format(type(msg)))

