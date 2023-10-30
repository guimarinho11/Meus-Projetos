class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_salario(self):
        return self.__salario


class Desenvolvedor(Funcionario):
    def __init__(self, nome, cpf, salario, tecnologias, horas_dev):
        Funcionario.__init__(self, nome, cpf, salario)
        self.__tecnologias = tecnologias
        self.__horas_dev = horas_dev

    def calculo_salario(self):
        return self.get_salario() * self.__horas_dev


class GerentedeProjetos(Funcionario):
    def __init__(self, nome, cpf, salario, projetos, horas_projetos):
        Funcionario.__init__(self, nome, cpf, salario)
        self.__projetos = projetos
        self.__horas_projetos = horas_projetos

    def calculo_salario(self):
        bonificacao = len(self.__projetos) * 1000
        return self.get_salario() + bonificacao


desenvolvedor = Desenvolvedor("Leonardo", "123.456.789-00", 4000, ["My SQL", "C#"], 6)
gerente = GerentedeProjetos("Danilo", "098.765.432-11", 8600, ["Projeto X", "Projeto 0", "Projeto A"], 8)

print(f"Salário do desenvolvedor {desenvolvedor.get_nome()}: R${desenvolvedor.calculo_salario()}")
print(f"Salário do Gerente {gerente.get_nome()}: R${gerente.calculo_salario()}")
