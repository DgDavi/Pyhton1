# Calculadora Utilizando Funções
def soma(a, b):
    print(a + b)
    
def subtracao(a, b):
    print(a - b)
        
def multiplicacao(a, b):
    print(a * b)
    
def divisao(a, b):
    print(a / b)

while True:
    try:
        num1 = float(input('Digite o primeiro número:  '))
        num2 = float(input('Digite o segundo número: '))
        print('Qual operação você deseja? ')
        operacao = int(input('[1]Soma, [2]Subtração, [3]Multiplicação, [4]Divisão: '))
    except ValueError:
        print('Você não digitou algo válido.')
        continue

    if operacao >= 5 or operacao <= 0:
        print('Você não escolheu uma operação válida')
        continue

    if operacao == 1:
        soma(num1, num2)
        
    elif operacao == 2:
        subtracao(num1, num2)
        
    elif operacao == 3:
        multiplicacao(num1, num2)
        
    elif operacao == 4:
        divisao(num1, num2)

    print('Você deseja sair?')
    saida = input('[s]im [n]ão')

    if saida == 's':
        break
    elif saida =='n':
        break
    else:
        print('Você não digitou algo válido')
        continue
