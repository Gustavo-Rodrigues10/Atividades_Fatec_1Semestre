# Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12km/l. Receber o tempo de percurso e a velocidade média
tempo_horas = float(input("Digite o tempo de percurso em horas: "))
velocidade_media = float(input("Digite a velocidade média em Km/h: "))
rendimento_kml = 12.0 

distancia_km = tempo_horas * velocidade_media
litros_gastos = distancia_km / rendimento_kml

print(f"A distância percorrida foi de: {distancia_km} km")
print(f"A quantidade de litros de combustível gastos é: {litros_gastos}")