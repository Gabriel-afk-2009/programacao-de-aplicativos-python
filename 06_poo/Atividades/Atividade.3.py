class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = float(saldo_inicial)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado! Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque de R$ {valor:.2f} recusado: Saldo insuficiente")
        elif valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado! Novo saldo: R$ {self.saldo:.2f}")

    def extrato(self):
        print(f"Titular: {self.titular} | Saldo Atual: R$ {self.saldo:.2f}")



conta1 = ContaBancaria("Maria Silva")


conta2 = ContaBancaria("João Santos", 500.0)

print("=== CONTA 1 (Sem saldo inicial informado) ===")
conta1.extrato()
conta1.depositar(150.00)

conta1.sacar(50.00)

conta1.sacar(200.00)
conta1.extrato()

print("\n" + "=" * 45 + "\n")

print("=== CONTA 2 (Saldo inicial de R$ 500) ===")
conta2.extrato()
conta2.depositar(250.00)

conta2.sacar(700.00)

conta2.sacar(100.00)
conta2.extrato()