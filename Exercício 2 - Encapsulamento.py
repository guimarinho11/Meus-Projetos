class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        self.__preco = novo_preco

    def valor_total(self, quantidade):
        return self.__preco * quantidade


class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = {}

    def adicionar_produto(self, produto, quantidade):
        if produto in self.__produtos:
            self.__produtos[produto] += quantidade
        else:
            self.__produtos[produto] = quantidade

    def remover_produto(self, produto):
        if produto in self.__produtos:
            del self.__produtos[produto]

    def valor_total(self):
        total = 0
        for produto, quantidade in self.__produtos.items():
            total += produto.get_preco() * quantidade
        return total

    def lista_de_produtos(self):
        return list(self.__produtos.keys())


produto1 = Produto("Camiseta", 50)
produto2 = Produto("Sabonete", 5)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(produto1, 2)
carrinho.adicionar_produto(produto2, 5)

valor_total = carrinho.valor_total()
print("Valor total do carrinho: R$", valor_total)

lista_produtos = carrinho.lista_de_produtos()
print("Lista de produtos no carrinho:")
for item in lista_produtos:
    produto, quantidade = item
    print(f"Produto: {produto.get_nome()}, Quantidade: {quantidade}")
