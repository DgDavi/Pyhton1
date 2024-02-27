#Calculadora Simmples

from math import pow

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

print("""Opções de operação:
[ 1 ] SOMA
[ 2 ] SUBTAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO
[ 5 ] POTENCIAÇÃO""")
escolha = int(input('Escolha o número da operação que deseja: '))
print('O resultado está abaixo')

if escolha == 1:
    print(numero1 + numero2)
elif escolha == 2:
    print(numero1 - numero2)
elif escolha == 3:
    print(numero1 * numero2)
elif escolha == 4:
    print(numero1 / numero2)
elif escolha == 5:
    print(pow(numero1, numero2))
else:
    print('VOCÊ NÃO ESCOLHEU UMA OPÇÃO VÁLIDA')