class Raquel():
    nome = "raquel"
    _idade = "15"
    __cpf = "42567"

    def getDados(self):
        print('Nome:' + self.nome)
        print('idade:' + self._idade)
        print('cpf:' + self.__cpf)

    def setAtr(self):
        self.nome = input("Digite um nome: ")
        self._idade = input("Digite uma idade: ")
        self.__cpf = input("Digite seu CPF: ")

    def falar(self):
        return "Hey There! Im using WhatsApp."