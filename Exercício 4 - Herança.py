class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome
        return novo_nome

    def get_vida(self):
        return self.vida

    def set_vida(self, nova_vida):
        self.vida = nova_vida
        return nova_vida

    def get_ataque(self):
        return self.ataque

    def set_ataque(self, novo_ataque):
        self.ataque = novo_ataque
        return novo_ataque

    def get_defesa(self):
        return self.defesa

    def set_defesa(self, nova_defesa):
        self.defesa = nova_defesa
        return nova_defesa


class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque, defesa, armadura):
        Personagem.__init__(self, nome, vida, ataque, defesa)
        self.armadura = armadura

    def atacar(self):
        print(f"O/A Guerreir@ {self.get_nome() or self.set_nome(self)}, atacou causando um dano de {self.get_ataque() or self.set_ataque(self) + self.armadura} ao oponente!")

    def defender(self):
        print(f"O/A Guerreir@ {self.get_nome() or self.set_nome(self)}, se defendeu "
              f"\n Vida = {self.get_vida() or self.set_vida(self) + self.armadura}")

    def descansar(self):
        print(f"O/A Guerreir@ {self.get_nome() or self.set_nome(self)} está descansado após uma batalha!")


class Mago(Personagem):
    def __init__(self, nome, vida, ataque, defesa, magia):
        Personagem.__init__(self, nome, vida, ataque, defesa)
        self.magia = magia

    def atacar(self):
        print(f"O Mago {self.get_nome() or self.set_nome(self)}, atacou causando um dano de {self.get_ataque() or self.set_ataque(self) + self.magia} ao oponente!")

    def descansar(self):
        print(f"O Mago {self.get_nome() or self.set_nome(self)} está descansando após uma batalha!")


guerreiro = Guerreiro("Matheus", 100, 75, 50, 10)
guerreiro.atacar()
guerreiro.defender()
guerreiro.descansar()

mago = Mago("Matheus", 100, 50, 75, 25)
mago.atacar()
mago.descansar()
