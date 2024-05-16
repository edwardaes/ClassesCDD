class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome= nome
        self.peso= peso
        self.idade= idade

    def comer(self, Comida, Bebida):
        print(F'{self.nome} Foi comer {Comida}, {Bebida}')

    def falar(self):
        print(f'{self.nome} está falando')

    def dormir(self):
        print(f'{self.nome} está dormindo')