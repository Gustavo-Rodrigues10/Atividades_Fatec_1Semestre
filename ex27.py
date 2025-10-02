# Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.
voltas_circuito = int(input("Digite o número de voltas: "))
extensao_circuito = float(input("Digite a extensão do circuito em metros: "))
tempo_total = float(input("Digite o tempo de duração em minutos: "))

distancia_total = (voltas_circuito * extensao_circuito) / 1000
tempo_horas = tempo_total / 60

velocidade_media = distancia_total / tempo_horas

print(f"A velocidade média foi de {velocidade_media} km/h.")
