# Receba a hora de início e de final de um jogo (HH,MM). Calcular o tempo do jogo em horas e minutos,
# sabendo que o tempo máximo é menor que 24 horas e pode começar num dia 
# e terminar no outro.
hora_inicial = int(input("Insira a hora de início: "))
minuto_inicial = int(input("Insira os minutos de início: "))
hora_final = int(input("Insira a hora de término: "))
minuto_final = int(input("Insira os minutos de término: "))

tempo_inicial = hora_inicial * 60 + minuto_inicial
tempo_final = hora_final * 60 + minuto_final

if tempo_final < tempo_inicial:
    tempo_final += 24 * 60

duracao_total = tempo_final - tempo_inicial
duracao_horas = duracao_total // 60
duracao_minutos = duracao_total % 60

print(f"A duração do jogo foi de {duracao_horas} hora(s) e {duracao_minutos} minuto(s).")
