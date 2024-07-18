from atividadee import Raquel

class Matheus(Raquel):
    __altura_cm = 0
    gosta_de = ''
    
    def setAtr(self):
        self.nome = input("Digite um nome: ")
        self._idade = input("Digite uma idade: ")
        self.__cpf = input("Digite um cpf: ")
        try:
            self.__altura = input("Digite uma altura em centímetros: ")
        except:
            print("Valor inválido. Digite um número inteiro.")
            self.__altura = input("Digite uma altura em centímetros: ")
        self.gosta_de = input("Digite uma coisa que tu gosta: ")
    
    def getDados(self):
        return '''nome = {self.nome}
idade = {_self._idade}
cpf = {self.__cpf}
altura em cm: {__self.alturacm}
{self.nome} gosta de {self.gosta_de}'''

    def gritar(self):
        return "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"