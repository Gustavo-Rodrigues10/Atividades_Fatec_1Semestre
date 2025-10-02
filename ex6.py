# Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.
valor_X = input("Insira o valor de X: ")
valor_Y = input("Insira o valor de Y: ")

print(f"Antes da troca: X = {valor_X} e Y = {valor_Y}")

valor_X, valor_Y = valor_Y, valor_X

print(f"Depois da troca: X = {valor_X} e Y = {valor_Y}")
