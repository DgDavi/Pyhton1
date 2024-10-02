logins = []

def cadastro():
  while True:
    try:
      login = input('Digite seu login com até 10 caracteres: ')
      if len(login) > 10:
        print('Login impossível.')
        continue
      elif login in logins:
        print('ERRO: Este login já foi cadastrado.')
        continue
      else:
        logins.append(login)
        print('Login cadastrado com sucesso.')

      while True:
        senha = input('Digite sua senha com 8 caracteres: ')
        if len(senha) != 8:
          print('Senha inválida.')
          continue
        else:
          print('Senha Cadastrada.')
          break
    except (ValueError, TypeError):
      print('Entrada inválida.')
      continue
    return 'Cadastro realizado com sucesso.'
    

def cadastros_feitos():
  if not logins:
    return 'Nenhum cadastro realizado ainda.'
  
  for i in logins:
    print(i)
  return 'Aqui estão todos os logins registrados.'

def menu():
  print('-------------------------------\n        Menu Principal\n-------------------------------')
  print('1 - Ver Pessoas Cadastrada\n2 - Cadastrar Nova Pessoa\n3 - Sair do Sistema')
  print('-------------------------------')
  while True:
    try: 
      opcao = int(input('Sua opção: '))
      if opcao in [1, 2, 3]:

        if opcao == 1:
          print('-------------------------------\n           OPÇÃO 1\n-------------------------------')
          return cadastros_feitos()
        elif opcao == 2:
          print('-------------------------------\n           OPÇÃO 2\n-------------------------------')
          return cadastro()
        elif opcao == 3:
          print('-------------------------------\n        Saindo do Sistema\n-------------------------------')
          break
      else:
        print('ERRO: Por favor, digite uma das opçóes válidas: 1, 2, 3.')

    except (ValueError, TypeError):
      print('ERRO: Por favor, digite uma das opções válidas: 1, 2, 3.')
      continue

menu()
