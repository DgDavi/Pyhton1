from random import randint
from time import sleep

num_computador = randint(0, 20)

def advinhar(num):
    print('Tente advinhar o número. O número deve estar entre 0 e 20.')
    sleep(0.5)
    rodadas = 0
    chutes_ocorridos = []

    while True:
      try:
        rodadas += 1
        if rodadas == 11:
          print(f'Você perdeu.\nO número era {num}')
          break

        print(f'Rodada: {rodadas}')

        chute_jogador = int(input('Chute: '))

        if not (0 <= chute_jogador <= 20):
          print('Chute apenas números inteiros de 0 a 20.')
          rodadas -= 1
          continue
        elif chute_jogador == num:
          print('Você acertou.')
          break

        if chute_jogador in chutes_ocorridos:
          print('Chute ja tentado. Tente novamente.')
          rodadas -= 1
          continue

        chutes_ocorridos.append(chute_jogador)
        print('Você errou.')
        continue

      except (ValueError, TypeError):
          print('Chute apenas números inteiros de 0 a 20.')
          rodadas -= 1
          continue

advinhar(num_computador)
