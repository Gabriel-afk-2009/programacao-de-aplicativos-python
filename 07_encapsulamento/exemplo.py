# 1. Encapsulamento
# Proteger o salário para que ele só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario  # atributo privado

    def apresentar(self):
        print(f"Sou {self.nome} e ganho {self.__salario}")

    @property                          # built-in do Python, sem import
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            print("Salário inválido!")
        else:
            self.__salario = valor

    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
            return
        self.__salario = self.__salario * (1 + porcentagem / 100)  # * faltava
        print(f"{self.nome} recebeu {porcentagem}% de aumento")


# 2. Herança

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def mostrar_equipe(self):           # indentado corretamente dentro da classe
        print(f"{self.nome} gerencia {self.equipe} pessoas")


class Estagiario(Funcionario):          # fora de Gerente, no nível correto
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso


# Testes
ana = Funcionario(nome="Ana", salario=1000)
ana.apresentar()
ana.dar_aumento(10)
ana.apresentar()

fulano = Gerente(nome="Fulano", salario=8000, equipe=6)
fulano.mostrar_equipe()

caio = Estagiario(nome="Caio", salario=5000, curso="Análise de Sistemas")
caio.apresentar()