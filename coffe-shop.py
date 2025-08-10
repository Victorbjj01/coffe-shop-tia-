# Coffee Shops Tia Rosa - Sistema de Atendimento

produtos = []
clientes = []
pedidos = []

# Cadastro de produtos
def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    codigo = input("Código do produto (ex: CAF01): ").upper()
    produtos.append({'nome': nome, 'preco': preco, 'codigo': codigo})
    print(f"Produto '{nome}' cadastrado com sucesso!\n")

# Lista de produtos
def listar_produtos_cadastrados():
    if not produtos:
        print("\nNenhum produto cadastrado.\n")
        return
    print("\nProdutos cadastrados:")
    for p in produtos:
        print(f"{p['codigo']} - {p['nome']} - R$ {p['preco']:.2f}")
    print()

# Cadrastro de clientes
def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    clientes.append({'nome': nome, 'cpf': cpf, 'telefone': telefone, 'email': email})
    print(f"Cliente '{nome}' cadastrado com sucesso!\n")

# Lista de Clientes
def listar_clientes():
    if not clientes:
        print("\nNenhum cliente cadastrado.\n")
        return
    print("\nClientes cadastrados:")
    for c in clientes:
        print(f"{c['nome']} - CPF: {c['cpf']} - Tel: {c['telefone']} - Email: {c['email']}")
    print()

#  Cardapio de bebidas
def mostrar_cardapio_bebidas():
    bebidas = {
        'bb1': {'nome': 'Café Espresso', 'descricao': 'Concentrado e forte.', 'preco': 5.0},
        'bb2': {'nome': 'Latte', 'descricao': 'Com leite vaporizado.', 'preco': 6.0},
        'bb3': {'nome': 'Cappuccino', 'descricao': 'Espuma de leite espessa.', 'preco': 7.0},
        'bb4': {'nome': 'Mocha', 'descricao': 'Com chocolate.', 'preco': 7.0},
        'bb5': {'nome': 'Chá Gelado', 'descricao': 'Chá servido com gelo.', 'preco': 6.0},
    }
    print('\nCardápio - Bebidas:')
    for cod, item in bebidas.items():
        print(f"{cod} - {item['nome']}: {item['descricao']} (R$ {item['preco']:.2f})")
    print()

# Cardapios de lanches
def mostrar_cardapio_lanches():
    lanches = {
        'lc1': {'nome': 'Pão de Queijo', 'descricao': 'Tradicional', 'preco': 3.0},
        'lc2': {'nome': 'Coxinha', 'descricao': 'Frango e catupiry', 'preco': 4.0},
        'lc3': {'nome': 'Quibe', 'descricao': 'De carne', 'preco': 3.5},
        'lc4': {'nome': 'Empada', 'descricao': 'Frango', 'preco': 4.0},
        'lc5': {'nome': 'Sanduíche Natural', 'descricao': 'Frango, alface, tomate', 'preco': 6.0},
    }
    print('\nCardápio - Lanches:')
    for cod, item in lanches.items():
        print(f"{cod} - {item['nome']}: {item['descricao']} (R$ {item['preco']:.2f})")
    print()

# Cardapio de doces
def mostrar_cardapio_doces():
    doces = {
        'dc1': {'nome': 'Brigadeiro', 'descricao': 'Chocolate', 'preco': 3.0},
        'dc2': {'nome': 'Bolo de Cenoura', 'descricao': 'Com cobertura de chocolate', 'preco': 4.0},
        'dc3': {'nome': 'Brownie', 'descricao': 'Chocolate com nozes', 'preco': 5.0},
        'dc4': {'nome': 'Donut', 'descricao': 'Recheado', 'preco': 5.0},
        'dc5': {'nome': 'Torta de Limão', 'descricao': 'Com merengue', 'preco': 5.0},
    }
    print('\nCardápio - Doces:')
    for cod, item in doces.items():
        print(f"{cod} - {item['nome']}: {item['descricao']} (R$ {item['preco']:.2f})")
    print()


# Pedidos
def fazer_pedido():
    if not produtos or not clientes:
        print("\nCadastre produtos e clientes antes de fazer pedidos.\n")
        return

    nome_cliente = input("Nome do cliente: ")
    cliente = next((c for c in clientes if c['nome'].lower() == nome_cliente.lower()), None)
    if not cliente:
        print("Cliente não encontrado.")
        return

    listar_produtos_cadastrados()
    codigos = input("Digite os códigos dos produtos (separados por vírgula): ").split(',')

    itens = []
    total = 0
    for codigo in codigos:
        codigo = codigo.strip().upper()
        produto = next((p for p in produtos if p['codigo'] == codigo), None)
        if produto:
            itens.append(produto)
            total += produto['preco']
        else:
            print(f"Produto com código '{codigo}' não encontrado.")

    if not itens:
        print("Nenhum item válido no pedido.")
        return

    pedidos.append({'cliente': cliente, 'itens': itens, 'total': total})
    print(f"\nPedido realizado para {cliente['nome']}! Total: R$ {total:.2f}\n")

# Pedidos do cardapio fixo
def fazer_pedido_cardapio_fixo():
    if not clientes:
        print("Cadastre um cliente antes de fazer um pedido.\n")
        return

    nome_cliente = input("Nome do cliente: ")
    cliente = next((c for c in clientes if c['nome'].lower() == nome_cliente.lower()), None)
    if not cliente:
        print("Cliente não encontrado.")
        return

    bebidas = {
        'BE1': {'nome': 'Café Espresso', 'preco': 5.0},
        'BE2': {'nome': 'Latte', 'preco': 6.0},
        'BE3': {'nome': 'Cappuccino', 'preco': 7.0},
        'BE4': {'nome': 'Mocha', 'preco': 7.0},
        'BE5': {'nome': 'Chá Gelado', 'preco': 6.0},
    }
    lanches = {
        'LC1': {'nome': 'Pão de Queijo', 'preco': 3.0},
        'LC2': {'nome': 'Coxinha', 'preco': 4.0},
        'LC3': {'nome': 'Quibe', 'preco': 3.5},
        'LC4': {'nome': 'Empada', 'preco': 4.0},
        'LC5': {'nome': 'Sanduíche Natural', 'preco': 6.0},
    }
    doces = {
        'DC1': {'nome': 'Brigadeiro', 'preco': 2.0},
        'DC2': {'nome': 'Bolo de Cenoura', 'preco': 4.0},
        'DC3': {'nome': 'Brownie', 'preco': 5.0},
        'DC4': {'nome': 'Donut', 'preco': 5.0},
        'DC5': {'nome': 'Torta de Limão', 'preco': 5.0},
    }

    cardapio_total = {**bebidas, **lanches, **doces}

    print("\nCardápio completo (fixo):")
    for cod, item in cardapio_total.items():
        print(f"{cod} - {item['nome']} (R$ {item['preco']:.2f})")
    print()

    codigos = input("Digite os códigos dos produtos desejados (separados por vírgula): ").split(',')

    itens = []
    total = 0
    for codigo in codigos:
        codigo = codigo.strip().upper()
        if codigo in cardapio_total:
            item = cardapio_total[codigo]
            itens.append(item)
            total += item['preco']
        else:
            print(f"Produto com código '{codigo}' não encontrado no cardápio fixo.")

    if not itens:
        print("Nenhum item válido no pedido.")
        return

    pedidos.append({'cliente': cliente, 'itens': itens, 'total': total})
    print(f"\nPedido realizado para {cliente['nome']}! Total: R$ {total:.2f}\n")

def listar_pedidos():
    if not pedidos:
        print("\nNenhum pedido realizado ainda.\n")
        return

    print("\nPedidos realizados:")
    for idx, pedido in enumerate(pedidos, start=1):
        nomes_produtos = ', '.join([item['nome'] for item in pedido['itens']])
        print(f"{idx}. Cliente: {pedido['cliente']['nome']} | Itens: {nomes_produtos} | Total: R$ {pedido['total']:.2f}")
    print()

#Menu essa e a parte que e vista no sistema quando está sendo executado no caso assim que o sistema estive rodando.
def menu():
    while True:
        print("Coffee Shops Tia Rosa ")
        print("1. Cadastrar produto")
        print("2. Listar produtos cadastrados")
        print("3. Cadastrar cliente")
        print("4. Listar clientes")
        print("5. Fazer pedido de produtos cadastrados")
        print("6. Fazer pedido do cardápio fixo")
        print("7. Listar pedidos")
        print("8. Ver cardápio de bebidas")
        print("9. Ver cardápio de lanches")
        print("10. Ver cardápio de doces")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos_cadastrados()
        elif opcao == "3":
            cadastrar_cliente()
        elif opcao == "4":
            listar_clientes()
        elif opcao == "5":
            fazer_pedido()
        elif opcao == "6":
            fazer_pedido_cardapio_fixo()
        elif opcao == "7":
            listar_pedidos()
        elif opcao == "8":
            mostrar_cardapio_bebidas()
        elif opcao == "9":
            mostrar_cardapio_lanches()
        elif opcao == "10":
            mostrar_cardapio_doces()
        elif opcao == "0":
            print("\nObrigado por usar o sistema da Tia Rosa. Até logo!\n")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
