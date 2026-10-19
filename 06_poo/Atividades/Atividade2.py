
#Atividades 2

class Livro:
    def __init__(self, titulo, autor, total_paginas):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.paginas_lidas = 0

    def ler(self, paginas):

        self.paginas_lidas = min(self.paginas_lidas + paginas, self.total_paginas)

    def porcentagem_lida(self):
        return (self.paginas_lidas / self.total_paginas) * 100

    def paginas_restantes(self):
        return self.total_paginas - self.paginas_lidas

    def terminou(self):
        return self.paginas_lidas == self.total_paginas

livro1 = Livro("Carrinhos", "John Lasseter", 300)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 200)

print(f"=== Lendo: {livro1.titulo} ({livro1.total_paginas} páginas) ===")
sessoes_livro1 = [80, 120, 150]

for paginas in sessoes_livro1:
    livro1.ler(paginas)
    pct = livro1.porcentagem_lida()
    restantes = livro1.paginas_restantes()
    status = "Sim" if livro1.terminou() else "Não"

    print(f"Lidas +{paginas} pág. | Progresso: {pct:.1f}% | Restam: {restantes} pág. | Terminou? {status}")

print("\n" + "=" * 50 + "\n")

print(f"=== Lendo: {livro2.titulo} ({livro2.total_paginas} páginas) ===")
sessoes_livro2 = [50, 50, 100]

for paginas in sessoes_livro2:
    livro2.ler(paginas)
    pct = livro2.porcentagem_lida()
    restantes = livro2.paginas_restantes()
    status = "Sim" if livro2.terminou() else "Não"

    print(f"Lidas +{paginas} pág. | Progresso: {pct:.1f}% | Restam: {restantes} pág. | Terminou? {status}")
