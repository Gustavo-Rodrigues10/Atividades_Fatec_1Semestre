# 41. Mostre todas as possibilidades de 2 dados de forma que a soma tenha como
# resultado 7.
def soma_dados_sete():
    dado1 = 1
    while dado1 <= 6:
        dado2 = 1
        while dado2 <= 6:
            if dado1 + dado2 == 7:
                print(f"Dado1 = {dado1}, Dado2 = {dado2} Soma = {dado1 + dado2}")
            dado2 += 1
        dado1 += 1

soma_dados_sete()
