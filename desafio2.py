
# Criando uma Lista 'itens' para armazenar os equipamentos:
itens = []

# Criando um loop para solicitar os itens ao usuário:
while len(itens) < 3:
    # Solicitando o item e armazenando na variável "item":
    item = input("Informe o nome de um equipamento: ")
    # Adicionando o item à lista "itens":
    itens.append(item)

# Exibindo a lista de itens
print("\nLista de Equipamentos:")
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")