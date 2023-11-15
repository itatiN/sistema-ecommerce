class Pessoa:
    def __init__(self, nome, endereco, idade, telefone, tipo, saldo):
        self.nome = nome
        self.endereco = endereco
        self.idade = idade
        self.telefone = telefone
        self.tipo = tipo
        self.__saldo = saldo


    def __atualizarEndereco(self, endereco):
        self.endereco = endereco

    def __atualizarTelefone(self, telefone):
        self.telefone = telefone
    
    def __atualizarSaldo(self, saldo):
        # É possivel colocar um atributo como privado
        # isso é usado em atributos que n devem ser mostrados para todos
        self.__saldo = saldo

    # Mesma ideia de encapsular funcoes para atualizar atributos

    def atualizarEndereco(self, endereco):
        self.__atualizarEndereco(endereco)

    def atualizarTelefone(self, telefone):
        self.__atualizarTelefone(telefone)

    def atualizarSaldo(self, saldo):
        self.__atualizarSaldo(saldo)
    
    def mostrarSaldo(self):
        print("Saldo: " + str(self.__saldo))


mock = Pessoa("Pessoa Mock", "Rua Mock", 20, "999999999", "Mock", 100.0)
mock.mostrarSaldo()