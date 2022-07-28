# Calculadora em Python_v1:
import math

soma = "1 - Soma"
subtracao = "2 - Subtração"
multiplicacao = "3 - Multiplicação"
divisao = "4 - Divisão"
enter = "\n"

Passo1 = "Selecione uma opção para continuar:" + enter + enter + soma + enter + subtracao + enter + multiplicacao + enter + divisao + enter

print(Passo1)

Passo2 = int(input("Digite a sua opção (1/2/3/4):"))

if Passo2 == 1:
    var1 = int(input("Digite o Primeiro Número:"))
    var2 = int(input("Digite o Segundo Número:"))
    print(str(var1), '+', str(var2), '=', var1 + var2)

elif Passo2 == 2:
    var1 = int(input("Digite o Primeiro Número:"))
    var2 = int(input("Digite o Segundo Número:"))
    print(str(var1), '-', str(var2), '=', var1 - var2)

elif Passo2 == 3:
    var1 = int(input("Digite o Primeiro Número:"))
    var2 = int(input("Digite o Segundo Número:"))
    print(str(var1), '*', str(var2), '=', var1 * var2)

elif Passo2 == 4:
    var1 = int(input("Digite o Primeiro Número:"))
    var2 = int(input("Digite o Segundo Número:"))
    print(str(var1), '/', str(var2), '=', var1 / var2)

elif Passo2 != 1 or 2 or 3 or 4:
    print("Opção inválida!\nFavor digitar uma opção dentre os números (1/2/3/4)")
