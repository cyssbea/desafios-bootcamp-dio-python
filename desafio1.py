# Solicitando ao usuario a média de consumo de Internet em "float"
consumo = float(input())

# Funcao que retorna o plano ideal para o cliente de acordo com o consumo informado pelo mesmo
def recomendar_plano(consumo):
    # Definindo os planos disponíveis
    pl_essencial = "Plano Essencial Fibra - 50Mbps"
    pl_prata = "Plano Prata Fibra - 100Mbps"
    pl_premium = "Plano Premium Fibra - 300Mbps"

    # Condições para recomendar o plano adequado
    if consumo <= 10:
        print(f"{pl_essencial}")
    elif consumo <= 20:
        print(f"{pl_prata}")
    else:
        print(f"{pl_premium}")
    

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado
recomendar_plano(consumo)

