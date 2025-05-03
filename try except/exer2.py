# verificação de data

from datetime import datetime

try:
    data = input('Digite uma data: (yyyy-mm-dd) ')
    datetime.strptime(data, '%Y-%m-%d')
    print('data válida!')

except ValueError:
    print('Data inválida!')