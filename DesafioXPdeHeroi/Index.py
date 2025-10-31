# Entrada de dados
nome_do_heroi = input("Como devemos lhe chamar, herói? ")
xp = int(input("Quanto de XP seu herói possui? "))

# Inicializando variáveis
nivel = ""
faixa = 0

# Loop para determinar o nível
while True:
    if xp < 1000:
        nivel = "Ferro"
        break
    elif xp <= 2000:
        nivel = "Bronze"
        break
    elif xp <= 5000:
        nivel = "Prata"
        break
    elif xp <= 7000:
        nivel = "Ouro"
        break
    elif xp <= 8000:
        nivel = "Platina"
        break
    elif xp <= 9000:
        nivel = "Ascendente"
        break
    elif xp <= 10000:
        nivel = "Imortal"
        break
    else:
        nivel = "Radiante"
        break

# Saída
print(f"Parabens {nome_do_heroi}, voçê está no nível de {nivel}.")