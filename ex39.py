# 39. Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
# Casa: 1 2 3 4 ... 64
# Qdte: 1 2 4 8 ... N
casa = 1
graos = 1

while casa <= 64:
    print(f"Casa {casa}: {graos} grãos")
    graos *= 2
    casa += 1
