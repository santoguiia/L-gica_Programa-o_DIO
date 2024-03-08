# Função para calcular o nível do jogador com base na quantidade de vitórias e derrotas
def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas
    
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    return saldo_vitorias, nivel

# Solicitar a quantidade de vitórias e derrotas do jogador
vitorias = int(input("Digite a quantidade de vitórias do jogador: "))
derrotas = int(input("Digite a quantidade de derrotas do jogador: "))

# Chamando a função para calcular o nível do jogador
saldo_vitorias, nivel = calcular_nivel(vitorias, derrotas)

# Exibir mensagem com o saldo de vitórias e o nível do jogador
print(f"O Herói tem um saldo de {saldo_vitorias} está no nível de {nivel}")
