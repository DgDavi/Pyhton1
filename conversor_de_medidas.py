def menu():
  print('----------- Bem Vindo -----------')
  print()
  print('Este é conversor de medidas.\nConversões possíveis:')
  print()
  print('Quilograma(kg) <--> Libra(lb)\nMetros(m) <--> Pés(ft)\nCelsius(c) <--> Fahrenheit(f)')
  print()
  

def conversor():
  menu()

  while True:
    try:
      numero = float(input('Digite o número a ser convertido: '))
      medida_inicial = input('Digite o símbolo da medida em que o número está: ')
      medida_final = input('Digite o símbolo da medida que deseja converter: ')

      if medida_inicial not in ['kg', 'lb', 'm', 'ft', 'c', 'f'] or medida_final not in ['kg', 'lb', 'm', 'ft', 'c', 'f']:
        print('Uma de suas medidas não é valida. Tente novamente.')
        continue
    except (ValueError, TypeError):
      print('Valor Inválido. Tente novamente.')
      continue

    if medida_inicial == 'kg' and medida_final == 'lb':
      conversao = numero * 2.205
      print(f'Seu número em Libras é {conversao:.2f}lb.')
    elif medida_inicial == 'lb' and medida_final == 'kg':
      conversao = numero / 2.205
      print(f'Seu número em Quilogramas é {conversao:.2f}kg.')
    elif medida_inicial == 'm' and medida_final == 'ft':
      conversao = numero * 3.28084
      print(f'Seu número em Pés é {conversao:.2f}ft.')
    elif medida_inicial == 'ft' and medida_final == 'm':
      conversao = numero * 0.3048
      print(f'O seu número em Metros é {conversao:.2f}m.')
    elif medida_inicial == 'c' and medida_final == 'f':
      conversao = (numero * 9/5) + 32
      print(f'Seu número em Fahrenheit é {conversao:.2f}f.')
    elif medida_inicial == 'f' and medida_final == 'c':
      conversao = (numero - 32) * 5/9
      print(f'Seu número em Celsius é {conversao:.2f}')
    else:
      print('Conversão impossivel. Tente novamente.')
      continue

    continuar = input('Deseja continuar? s/n ').lower()
    if continuar != 's':
      print('Conversor encerrado.')
      break   


conversor()
