from random import randint

num_computador = randint(0, 20)

def advinhar(num):
    rodadas = 0
    while True:
        try:

            rodadas += 1
            if rodadas == 11:
                print(f'Você perdeu.\nO número era {num}')
                break

            print(f'Rodada: {rodadas}')

            chute_jogador = int(input('Chute: '))

            if not (0 <= chute_jogador <= 20):
                print('Chute apenas números inteiros de 0 à 20.')
                rodadas -= 1
                continue
            elif chute_jogador == num:
                print('Você acertou.')
                break

            print('Você errou.')
            continue

        except (ValueError, TypeError):
            print('Chute apenas números inteiros de 0 à 20.')
            rodadas -= 1
            continue

advinhar(num_computador)
