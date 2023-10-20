import time

print('**************** CALCULADORA PYTHON ****************')

time.sleep(1)

nome = input('Digite seu nome: ')
print('Olá {}, tudo bem com você?\n[1] ADIÇÃO \n[2] SUBTRAÇÃO \n[3] MULTIPLICAÇÃO \n[4] DIVISÃO '.format(nome))

ope = int(input('Escolha o número referente a operação desejada: '))

if ope == 1 or 2 or 3 or 4:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número:'))


    if ope == 1:
        resultado =  num1 + num2
        print('O resultado da sua operação é: ',resultado)
    elif ope == 2:
        resultado = num1 - num2
        print('O resultado da sua operação é: ',resultado)
    elif ope == 3:
        resultado = num1 * num2
        print('O resultado da sua operação é: ',resultado)
    elif ope == 4:
        restultado = num1 / num2
        print('O resultado da sua operação é: ',restultado)
