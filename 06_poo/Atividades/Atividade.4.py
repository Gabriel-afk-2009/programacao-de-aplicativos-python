class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.nivel = 1

    def receber_dano(self, valor):
        self.vida = max(0, self.vida - valor)
        print(f"{self.nome} recebeu {valor} de dano. Vida atual: {self.vida}")
        if self.vida == 0:
            print(f"{self.nome} foi derrotado!")

    def curar(self, valor):
        if self.vida == 0:
            print(f"{self.nome} está derrotado e não pode ser curado!")
            return

        self.vida = min(100, self.vida + valor)
        print(f"{self.nome} foi curado em {valor} pontos. Vida atual: {self.vida}")

    def subir_nivel(self):
        self.nivel += 1
        self.vida = 100
        print(f"✨ {self.nome} subiu para o nível {self.nivel}! Vida restaurada para 100.")

    def status(self):
        print(f"Nome: {self.nome} | Classe: {self.classe} | Nível: {self.nivel} | Vida: {self.vida}/100")



p1 = Personagem("Aragorn", "Guerreiro")
p2 = Personagem("Gandalf", "Mago")

print("=== STATUS INICIAL ===")
p1.status()
p2.status()

print("\n=== SIMULANDO COMBATE ===")


p1.receber_dano(40)
p1.curar(20)
p1.curar(50)
p1.subir_nivel()
p1.status()

print("\n" + "=" * 45 + "\n")


p2.receber_dano(60)
p2.receber_dano(50)
p2.status()