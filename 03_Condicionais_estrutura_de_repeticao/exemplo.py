#1 . Estrutura Condicionais

nota = 6

if nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Reprovado')
else:
    print('Reprovado')

# 2. Condicionais e Operadires Lógicos
#and -> Todas as condições devem ser verdadeiras
#or -> Pelo menos uma condição deve ser verdadeira
#bot -> inverte o resultado

idade = 20
ingresso = 30

if idade >= 18 and ingresso:
    print("Entrada Permitida")
else:
    print("Entrada não Permitida")

#3. Estrutura de Repetição while

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

#4. estrutura de Repetição for

for numero in range(1, 6):
    print(numero)

#5. Percorrendo uma lista

Nomes = ["ana", "carlos", "joão", "Maria"]

for nome in Nomes:
    print(nome)

# 6. Break, Continue, Pass

for numero in range(1, 11):

    if numero == 6 :
        break