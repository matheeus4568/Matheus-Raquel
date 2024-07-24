from atividadee import Raquel

#RODAR ESTE ARQUIVO

class Matheus(Raquel):
    __altura_cm = 0
    gosta_de = ''

    def setAtr(self):
        self.nome = input("Digite um nome: ")
        self._idade = input("Digite uma idade: ")
        self.__cpf = input("Digite um cpf: ")
        self.__altura_cm = int(input("Digite uma altura em centímetros: "))
        self.gosta_de = input("Digite uma coisa que tu gosta: ")

    def getDados(self):
        print('Nome:' + self.nome)
        print('idade:' + self._idade)
        print('cpf:' + self.__cpf)
        print("altura em cm:", self.__altura_cm)
        print(self.nome + "gosta de:" + self.gosta_de)

    def gritar(self):
        return '''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'''


teste = Matheus()
teste.setAtr()
teste.getDados()
print(teste.gritar())
print(teste.falar())
