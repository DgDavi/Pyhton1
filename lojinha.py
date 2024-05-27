produtos = [
    {
        'Produto': 'Arroz',
        'Preço': 7.00,
        'Quantidade': 10
    },
    {
        'Produto': 'Feijão',
        'Preço': 10.00,
        'Quantidade': 12
    },
    {
        'Produto': 'Açúcar',
        'Preço': 5.00,
        'Quantidade': 8
    },
    {
        'Produto': 'Picanha',
        'Preço': 10.00,
        'Quantidade': 7
    },
    {
        'Produto': 'Coca-Cola',
        'Preço': 8.50,
        'Quantidade': 5
    }
]

login = ''
senha = ''

def menu_inicial():
    return """--=--=--=--=--=--=--=--=--=--=--
  Bem-Vindo à LOJINHA DO DAVI
--=--=--=--=--=--=--=--=--=--=--"""


def tabela_produtos():
    return '''Nossos produtos são os seguintes: 
Arroz: R$ 7.00, ID 0
Feijão: R$ 10.00, ID 1
Açúcar: R$ 5.00, ID 2
Picanha: R$ 10.00, ID 3
Coca-Cola: R$ 8.50, ID 4
'''


print(menu_inicial())

try:
    entrada = int(input('Digite 1 para Login ou 0 para Entrar: '))
except ValueError:
    print('Opção inválida')
    entrada = int(input('Digite 1 para Login ou 0 para Entrar: '))


if entrada != 1 and entrada != 0:
    while entrada != 1 or entrada != 0:
        print('Digite apenas 1 ou 0 para respectivamente Login e Entrar')
        entrada = input('')

if entrada == 1:
    login = input('Digite o usuário com 5 DIGITOS: ')
    qtd_letra_login = len(login)
    while len(login) > 5 or len(login) < 5:
        print('Usuário Inválido. DEVE CONTER 5 DIGITOS.')
        login = input('Digite o usuário: ')
        qtd_letra_login = len(login)
    
    senha = input('Digite a senha com 8 DIGITOS: ')
    qtd_digito_senha = len(senha)
    while len(senha) < 8 or len(senha) > 8:
        print('Senha inválida. DEVE CONTER 8 DIGITOS')
        senha = input('Digite a senha: ')
        qtd_digito_senha = len(senha)
        
if entrada == 0:
    login_entrada = input('Digite o usuário: ')
    while login_entrada != login:
        print('Usuário incorreto.')
        login_entrada = input('Tente novamente:')

    senha_entrada = input('Digite a senha: ')
    while senha_entrada != senha:
        print('Senha inválida.')
        senha_entrada = input('Tente novamente: ')

print(tabela_produtos())

compra_produto = int(input('Digite o ID do produto que deseja comprar: '))
while compra_produto > 5:
    print('ID não encontrado')
    compra_produto = int(input('Digite o ID novamente: '))

compra_quantidade = int(input('Digite a quantidade que você deseja comprar: '))

if compra_quantidade < produtos[compra_produto]['Quantidade']:
    print(f'Não temos essa quantidade. Possuímos apenas {produtos[compra_produto]["Quantidade"]} ')
    compra_quantidade = int(input('Digite novamente a quantidade que deseja comprar: '))

valor = compra_quantidade * produtos[compra_produto]['Preço']
print(f'O valor da sua compra ficou R$ {valor}')

saldo = float(input('Digite seu saldo para efetuara a comprar: R$ '))
while saldo < valor:
    print('Saldo insuficiente. Compra cancelada.')
    saldo = int(input('Digite o saldo novamente para comprar: '))

print('Compra efetuada com sucesso!')

produtos[compra_produto]['Quantidade'] -= compra_quantidade
