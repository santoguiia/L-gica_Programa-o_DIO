class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'usou magia'
        elif self.tipo == 'guerreiro':
            ataque = 'usou espada'
        elif self.tipo == 'monge':
            ataque = 'usou artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'usou shuriken'
        else:
            ataque = 'usou um ataque desconhecido'
        
        print(f"O {self.tipo} atacou usando {ataque}")

# Exemplo de utilização da classe Heroi
heroi1 = Heroi('Gandalf', 1500, 'mago')
heroi1.atacar()

heroi2 = Heroi('Aragorn', 35, 'guerreiro')
heroi2.atacar()

heroi3 = Heroi('Bruce Lee', 35, 'monge')
heroi3.atacar()

heroi4 = Heroi('Hattori Hanzo', 45, 'ninja')
heroi4.atacar()
