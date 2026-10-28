class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)
        print(f"'{produto.nome}' adicionado ao carrinho.")

    def total(self):
        return sum(item.subtotal() for item in self.itens)

    def mostrar(self):
        print("\n=== RESUMO DA COMPRA ===")
        if not self.itens:
            print("O carrinho está vazio.")
            return

        for item in self.itens:
            print(f"- {item.nome} | R$ {item.preco:.2f} x {item.quantidade} = R$ {item.subtotal():.2f}")

        print("-" * 40)
        print(f"TOTAL DA COMPRA: R$ {self.total():.2f}")



p1 = Produto("Café 500g", 18.50, 2)
p2 = Produto("Leite 1L", 4.80, 4)
p3 = Produto("Pão de Forma", 8.90, 1)
p4 = Produto("Queijo Mussarela 200g", 12.00, 3)


meu_carrinho = Carrinho()

print("--- Adicionando produtos ao carrinho ---")
meu_carrinho.adicionar(p1)
meu_carrinho.adicionar(p2)
meu_carrinho.adicionar(p3)
meu_carrinho.adicionar(p4)


meu_carrinho.mostrar()