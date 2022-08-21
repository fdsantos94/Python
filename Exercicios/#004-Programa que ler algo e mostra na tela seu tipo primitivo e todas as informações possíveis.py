# Programa que ler algo e mostra na tela seu tipo primitivo e algumas as informações possíveis
msg = input('Digite alguma coisa: ')

print('O valor digitado é numérico?', msg.isnumeric())
print('O valor digitado é alfabético?', msg.isalpha())
print('O valor digitado é alfanumerico?', msg.isalnum())
print('O valor digitado está em maiusculo?', msg.isupper())
print('O valor digitado está em minuscula?', msg.islower())
print('O valor digitado só tem espaços?', msg.isspace())
