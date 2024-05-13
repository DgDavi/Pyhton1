#Jokenpo
from random import choice
from time import sleep 

while True:
    opcoes = ['pedra', 'papel', 'tesoura']
    sorteio = choice(opcoes)


    print("""[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura""")
    try:
        jogador = float(input('Digite o número de acordo com a sua jogada:'))
    except ValueError:
        print('Você não digitou algo válido. Tente novamente.')
        sleep(0.8)
        continue

    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(0.2)

    print(f'O computador jogou {sorteio}')

    if jogador == 1:
        if sorteio == 'pedra':
            print('EMPATE!')
        elif sorteio == 'papel':
            print('VOCÊ PERDEU')
        elif sorteio == 'tesoura':
            print('VOCÊ GANHOU')
        else:
            print('JOGADA INVÁLIDA!')
        
    if jogador == 2:
        if sorteio == 'pedra':
            print('VOCÊ GANHOU!') 
        elif sorteio == 'papel':
            print('EMPATE!')
        elif sorteio == 'tesoura':
            print('VOCÊ PERDEU!')
        else:
            print('JOGADAD INVÁLIDA!')

    if jogador == 3:
        if sorteio == 'pedra':
            print('VOCÊ PERDEU!')
        elif sorteio == 'papel':
            print('VOCÊ GANHOU')
        elif sorteio == 'tesoura':
            print('EMPATE!')

    print('Você deseja sair?')
    saida = input('[s]im [n]ão')
    
    if saida == 's':
        print('Fim de Jogo!')
        break
    elif saida == 'n':
        continue
    else:
        print('Você não digitou algo válido. O jogo contiuará.')
        sleep(0.8)
        continue
