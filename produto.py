class Produto:
    def __init__(self, nome, preco, descricao, tipo):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.tipo = tipo
    
    # Nao faz sentido colocar id de forma estatica
    # teoricamente o id deveria ser gerado pelo banco de dados
    # ou ser o index de um array

    def __Informacoes(self) -> str:
        print("Nome: " + self.nome)
        print("Preço: " + str(self.preco))
        print("Descrição: " + self.descricao)
        print("Tipo: " + self.tipo)
        print("\n")

    # Ao declarar um obejto voce pode acessar os atributos dele
    # com isso voce pode mudar o valor deles.
    # Seguindo o principio S do SOLID uma funcao pode fazer apenas uma coisa
    # Logo voce tem que criar uma funcao para mudar cada atributo

    def __atualizarPreco(self, novoPreco):
        self.preco = novoPreco

    # Boas praticas de encapsulamento

    def exibeInformacoes(self):
        self.__Informacoes()

    def atualizaPreco(self, novoPreco):
        self.__atualizarPreco(novoPreco)


# conceito de mock:
# objeto com o intuito de simular um objeto real

mock = Produto("Produto Mock", 10.0, "Este e um produto Mock", "Mock")
mock.exibeInformacoes()
mock.atualizaPreco(20.0)
mock.exibeInformacoes()