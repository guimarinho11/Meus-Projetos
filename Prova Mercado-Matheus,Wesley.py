import mysql.connector

host = "167.99.252.245"
user = "ESW2023_E5"
passwd = "adm!n2023"
database = "ESW2023_E5_PROVA_LIMAS_GUIMAS"

conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
cursor = conector.cursor()


# Aqui será a parte onde os novos produtos serão inseridos no banco!
def inserir():
    print("\nAqui é a aba para inserir os novos produtos !")
    produto = input("Qual produto vai ser inserido? ")
    preco = input("Qual o preço desse produto? ")
    qtd_estoque = input("Qual o estoque atual desse produto? ")

# Dados sendo fornecidos ao banco:
    cursor.execute(f''' INSERT INTO TabelaProdutos (produto, preco , QTD_noEstoque) 
                        VALUES ('{produto}', {preco}, {qtd_estoque}) ''')
    conector.commit()


# Aqui será a parte onde você pode atualizar os seus dados!
def atualizar():
    print("\nAqui é a aba para atualizar um produto !")
    produto = input("Qual produto você quer atualizar? ")
    preco_novo = input("Qual o preço desse produto? ")
    estoque_novo = input("Qual o estoque a atualizar? ")

    # Informações sendo concedidas ao banco!
    cursor.execute(f''' UPDATE TabelaProdutos SET preco = '{preco_novo}' WHERE produto = '{produto}' ''')
    cursor.execute(f''' UPDATE TabelaProdutos SET QTD_noEstoque = '{estoque_novo}' WHERE produto = '{produto}' ''')
    conector.commit()


# Aqui você pode excluir algum produto!
def excluir():
    print("Você entrou na aba para deletar algum produto !")
    produto = input("Qual produto você deseja deletar? ")
    cursor.execute(f''' DELETE FROM TabelaProdutos WHERE produto = '{produto}' ''')
    conector.commit()


# Aqui é o modo caixa, onde o vendedor que está fazendo o procedimento de venda lá no caixa do hipermercado vai conceder
# algumas informações pro banco!
def caixa():
    print("Você entrou no modo caixa!")
    nome_cliente = input("Qual o nome do Cliente? ")
    nome_vendedor = input("Qual o nome da pessoa que fez a venda desses produtos? ")
    qtd_comprada = input("Quantidade de produto vendido? ")
    qtd_vendida = input("Quantidade de produto adquirido pelo cliente? ")

    # Os dados sendo adicionados no banco!
    cursor.execute(f''' INSERT INTO TabelaMercado (nome_cliente, QTD_comprada , nome_vendedor , QTD_vendida) 
    VALUES ('{nome_cliente}', {qtd_comprada}, '{nome_vendedor}', {qtd_vendida}) ''')
    conector.commit()


# E aqui será o menu principal, onde você poderá escolher o que fazer!
def menu_principal():
    inicio = True
    while inicio:
        print("\nSGBD -- Hipermercado Ponta da Pedra")
        print("1. Inserir novo produto")
        print("2. Atualizar produtos")
        print("3. Deletar produto")
        print("4. Modo caixa")
        opcao = input("Selecione o que você deseja fazer?: >>> ")
        if opcao == "1":
            inserir()
        elif opcao == "2":
            atualizar()
        elif opcao == "3":
            excluir()
        elif opcao == "4":
            caixa()
        else:
            inicio = False


menu_principal()
