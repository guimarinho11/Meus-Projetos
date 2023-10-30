import pymongo
import json
# Importando as bibliotecas, pymongo e json

class CRUD:
    def __init__(self, Cargas, Informacoes):  # Aqui conectei o Python com o mongoDB.
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient[Cargas]
        self.mycol = self.mydb[Informacoes]

    def ImportarDados(self, arquivoJSON):  # Aqui será onde vamos importar o nosso arquivo.txt para o mongoDB.
        try:
            with open(arquivoJSON, "r") as load:
                conteudo = load.read()
                conteudoJSON = json.loads(conteudo)
                self.mycol.insert_many(conteudoJSON)
                print("Arquivo JSON foi carregado com sucesso!\n")
        except FileNotFoundError:
            print("Arquivo JSON não encontrado.\n")
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.\n")


    def CriarDados(self, NotaFiscal, remetente, destinatario, endereco, carga, valor):  # Aqui serão criados os novos dados na collection do mongoDB.
        info = {"Numero da Nota Fiscal": NotaFiscal, "Remetente": remetente, "Destinatario": destinatario, "Endereco": endereco, "Carga": carga, "Valor": valor}
        x = self.mycol.insert_one(info)

    def LerDados(self, var, valor):  # Aqui você poderá ler os dados de acordo com qual informação você deseja.
        myquery = {var: valor}
        mydoc = self.mycol.find(myquery)
        for x in mydoc:
            print(x)

    def ModificarDados(self, varMod, valorMod, varNovo, valorNovo):  # Aqui você pode editar os seus dados de acordo com qual dado específico você quer mudar.
        filter = {varMod: valorMod}
        novo = {"$set": { varNovo: valorNovo }}
        self.mycol.update_many(filter, novo)

    def DeletarDados(self, variavel, valor):  # Aqui você pode deletar alguma informação do banco.
        myquery = {variavel: valor}
        self.mycol.delete_many(myquery)

def menu():
    global crud
    print("Seja bem-vindo ao programa CRUD da CPL S/A!\n")  # Aqui será o menu onde você pode interagir com o banco de dados.
    print("1. Configurar database e collection")  # A cada vez que você começar o programa, terá que configurar o banco, colocando qual a Data Base (Cargas) e a Collection (Informacoes).
    print("2. Importar dados (JSON)")  # Aqui você pode importar o arquivo JSON que está junto no arquivo zip.
    print("3. Criar dados")  # Aqui você pode criar novos dados no Banco.
    print("4. Ler dados")  # Aqui o programa irá printar para você a tabela com as informações que você colocar.
    print("5. Modificar dados")  # Aqui você poderá editar os dados.
    print("6. Deletar dados")  # Aqui você irá deletar os dados.
    opcao = input("--> ")

    if (opcao == "1"):
        Cargas = input("Qual a DataBase que você quer operar? ")
        Informacoes = input("Qual a Collection que você quer operar? ")
        crud = CRUD(Cargas, Informacoes)
        menu()

    if (opcao == "2"):
        arquivo = input("Qual o nome e extensão do arquivo JSON? ")
        crud.ImportarDados(arquivo)
        menu()

    if (opcao == "3"):
        NotaFiscal = input("Insira o Número da Nota Fiscal-> ")
        remetente = input("Insira o Remetente-> ")
        destinatario = input("Insira o Destinatário-> ")
        endereco = input("Insira o Endereço-> ")
        carga = input("Insira o Tipo de Carga-> ")
        valor = input("Insira o Valor-> ")
        crud.CriarDados(NotaFiscal, remetente, destinatario, endereco, carga, valor)
        menu()

    if (opcao == "4"):
        var = input("Qual a componente você deseja procurar? ")
        valor = input("Qual o valor deste componente? ")
        crud.LerDados(var, valor)
        menu()

    if (opcao == "5"):
        varModificar = input("Qual componente você deseja modificar? ")
        valorModificar = input("Qual o valor deste componente? ")
        varNovo = input("Qual novo nome deste componente? ")
        valorNovo = input("Qual o novo valor deste componente? ")
        crud.ModificarDados(varNovo, valorModificar, varModificar, valorNovo)
        menu()

    if (opcao == "6"):
        variavel = input("Qual o componente da(s) linha(s) deletada(s)? ")
        valor = input("Qual o valor deste(s) componente(s)? ")
        crud.DeletarDados(variavel, valor)
        menu()

menu()
