#Atividades 1

class cachorro:
    def __init__(self, nome, raca=None, idade=0):
        self.nome = nome
        self.raca = raca
        self.idade = idade

def latir(self):
    print(f"{self.nome}diz: Au Au!")

def mostrar_info(self):
    print(f"Nome: {self.nome} | Raca: {self.raca} | Idade: {self.idade}")

cachorro1 = cachorro(nome = "Rex", raca = "Pitbull", idade = 20)
cachorro2 = cachorro(nome = "BOB", raca = "chowchow", idade = 10)

print(mostrar_info(cachorro1))
print(mostrar_info(cachorro2))
