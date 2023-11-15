class Cliente:
    def __init__(self, nome, endereco, numero):
        self.nome = nome
        self.endereco = endereco
        self.numero = numero

    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}'