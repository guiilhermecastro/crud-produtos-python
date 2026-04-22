from database import conectar, criar_tabela

def listarProdutos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    if len(produtos) == 0:
        print('Não tem produtos cadastrados')
    for p in produtos:
        print(f'[{p[0]}] {p[1]} ... R$ {p[2]:.2f}')

def adicionarProduto(nome, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
    conn.commit()
    conn.close()
    print('Produto adicionado com sucesso!')

def buscarProduto(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE LOWER(nome) = LOWER(?)", (nome,))
    produto = cursor.fetchone()
    conn.close()
    return produto

def atualizarProduto(id, novo_nome, novo_preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE produtos SET nome = ?, preco = ? WHERE id = ?", (novo_nome, novo_preco, id))
    conn.commit()
    conn.close()
    print('Produto atualizado com sucesso!')

def removerProduto(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print('Produto removido com sucesso!')

opcao = None
criar_tabela()
while opcao != '0':
    print()
    print('========================================')
    print('               MENU')
    print('========================================')
    print('1 - Listar Produtos')
    print('2 - Adicionar Produto')
    print('3 - Buscar Produto')
    print('4 - Atualizar Produto')
    print('5 - Remover Produto')
    print('0 - Sair')
    print('========================================')

    if opcao == '1':
        print()
        print('LISTA DE PRODUTOS ======================')
        listarProdutos()

    elif opcao == '2':
        print()
        print('ADICIONAR PRODUTO ======================')
        nome = input('Nome: ')
        preco = float(input('Preço: '))
        adicionarProduto(nome, preco)
        print()
        print('LISTA DE PRODUTOS ======================')
        listarProdutos()

    elif opcao == '3':
        print()
        print('BUSCAR PRODUTO =========================')
        nome = input('Nome do produto: ')
        produto = buscarProduto(nome)
        if produto:
            print(f'Produto encontrado: [{produto[0]}] {produto[1]} ... R$ {produto[2]:.2f}')
        else:
            print('Produto não encontrado.')

    elif opcao == '4':
        print()
        print('ATUALIZAR PRODUTO ======================')
        nome = input('Nome do produto a atualizar: ')
        produto = buscarProduto(nome)
        if produto:
            novo_nome = input('Novo nome: ')
            novo_preco = float(input('Novo preço: '))
            atualizarProduto(produto[0], novo_nome, novo_preco)
            print()
            print('LISTA DE PRODUTOS ======================')
            listarProdutos()
        else:
            print('Produto não encontrado.')

    elif opcao == '5':
        print()
        print('REMOVER PRODUTO ========================')
        nome = input('Nome do produto a remover: ')
        produto = buscarProduto(nome)
        if produto:
            removerProduto(produto[0])
            print()
            print('LISTA DE PRODUTOS ======================')
            listarProdutos()
        else:
            print('Produto não encontrado.')

    elif opcao != None:
        print('Opção não existe')

    print()
    opcao = input('Opção desejada: ')