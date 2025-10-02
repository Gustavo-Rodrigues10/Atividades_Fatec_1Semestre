# Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
alimento_kg = float(input("Digite a quantidade de alimento em quilos (Kg): "))
consumo_g_dia = 50.0
fator_conversao = 1000.0

alimento_g = alimento_kg * fator_conversao
duracao_dias = alimento_g / consumo_g_dia

print(f"O alimento durará por: {duracao_dias} dias")