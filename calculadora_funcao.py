def soma(a, b):
    print(a + b)
    
def subtracao(a, b):
    print(a - b)
        
def multiplicacao(a, b):
    print(a * b)
    
def divisao(a, b):
    print(a / b)
    
num1 = float(input('Digite o primeiro número:  '))
num2 = float(input('Digite o segundo número: '))
print('Qual operação você deseja? ')
operacao = int(input('[1]Soma, [2]Subtração, [3]Multiplicação, [4]Divisão: '))

if operacao == 1:
    soma(num1, num2)
    
elif operacao == 2:
    subtracao(num1, num2)
    
elif operacao == 3:
    multiplicacao(num1, num2)
    
elif operacao == 4:
    divisao(num1, num2)