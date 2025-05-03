# Conversão segura de número:

try:
    numero = float(input('Digite um número: '))
    print('Realmente é numero!')
except ValueError:
    print('Não é numero!')