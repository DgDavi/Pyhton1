# Jokenpo

from os import system
from random import randint
from time import sleep

while True:
    item = ('Pedra', 'Papel', 'Tesoura') 
    computador = randint(0, 2)
    try:
        print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
        jogador = int(input('Qual a sua jogada? '))
    except ValueError:
        system('cls')
        print('Digite apenas os números abaixo referente as jogadas.')
        continue
     
    if jogador >= 3 or jogador < 0:
        system('cls')
        print('Digite apenas os números abaixo referente as jogadas.')
        continue
        	
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(0.5)

    print('-=' * 11)
    print(f'O computador jogou {(item[computador])}.')
    print(f'O jogador jogou {(item[jogador])}.')
    print('-=' * 11)

    if computador == 0:
        if jogador == 0:
                    print('EMPATE')
        elif jogador == 1:
                    print('JOGADOR VENCE')
        elif jogador == 2:
                    print('COMPUTADOR VENCE')
        else:
                    print('JOGADA INVALIDA')

    if computador == 1:
        if jogador == 0:
                print('COMPUTADOR VENCE')
        elif jogador == 1:
                print('EMPATE')
        elif jogador == 2:
                print('JOGADOR VENCE')
        else:
                print('JOGADA INVALIDA')
        
    if computador == 2:
        if jogador == 0:
                print('JOGADOR VENCE')
        elif jogador == 1:
                print('COMPUTADOR VENCE')
        elif jogador == 2:
                print('EMPATE')
        else:
                print('JOGADA INVALIDA')
                
    print('Você quer parar?')
    saida = input('[s]im [n]ão: ')
    
    if saida == 's':
        system('cls')
        break
    
    elif saida == 'n':
        continue
    
    else:
        system('cls')
        print('Você não digitou algo válido, o jogo continuará.')
        continue
