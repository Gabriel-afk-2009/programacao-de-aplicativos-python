#1. Encapsulamento
#Proteger o salário para que ele so mude seguindo regras
from msilib.schema import Property


class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.saldo = salario

        def apresentar(self):
            print(f"Sou{self.nome} e ganho {self.salario}")

        @Property
        def salario(self):
            return self.__salario

def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
            return
        self.__salario = self.__salario(1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento")



ana = funcionario(nome="Ana", salario=1000)
ana.apresentar()

