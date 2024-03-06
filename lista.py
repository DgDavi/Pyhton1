#Criar Lista

import os
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        try:
            os.system('cls')
            indice = int(input('Qual o indice que deseja apagar? '))
            del lista[indice]
        except ValueError:
            print('Digite apenas números inteiros.')

        except IndexError:
            print('Este índice não existe na lista.')

    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Não há nada para listar.')

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Escolha i, a ou l.')
