import datetime

try:
    data = input('Digite uma data: (yyyy-mm-dd) ')
    print(datetime.strptime(data, '%Y-%m-%d'))


except ValueError:
    print('Data inválida!')