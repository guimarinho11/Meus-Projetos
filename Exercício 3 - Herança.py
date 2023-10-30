class Pessoa:
    def __init__(self, nome, idade, endereco, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        return novo_nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        self.__idade = nova_idade
        return nova_idade

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, novo_endereco):
        self.__endereco = novo_endereco
        return novo_endereco

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, novo_telefone):
        self.__telefone = novo_telefone
        return novo_telefone


class Professor(Pessoa):
    def __init__(self, nome, idade, endereco, telefone, salario, disciplina):
        Pessoa.__init__(self, nome, idade, endereco, telefone)
        self.__salario = salario
        self.__disciplina = disciplina

    def dar_aula(self):
        print(f"Boa noite alunos, meu nome é {self.get_nome()}, e dou aula sobre {self.__disciplina}!")


class Aluno(Pessoa):
    def __init__(self, nome, idade, endereco, telefone, matricula, curso):
        Pessoa.__init__(self, nome, idade, endereco, telefone)
        self.__matricula = matricula
        self.__curso = curso

    def estudar(self):
        print(f"Olá, eu sou o {self.get_nome()}, e estou estudando {self.__curso}!")


professor = Professor("Matheus", 45, "Rua 1", 31442673546, 3000, "Matemática")
professor.dar_aula()
aluno = Aluno("Matheus", 15, "Rua 2", 172883949273, 12345, "Ferramentaria")
aluno.estudar()
