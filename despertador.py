import datetime
import time
import winsound  # Biblioteca nativa do Windows para emitir bipes


def despertar(hora_alarme):
    print(f"Alarme configurado para as {hora_alarme}")

    while True:
        # Pega o horário atual e formata para Hora:Minuto
        agora = datetime.datetime.now().strftime("%H:%M")

        # Compara a hora atual com a hora do alarme
        if agora == hora_alarme:
            print("Hora de acordar! Beep! Beep!")
            # Emite um bipe de 1000Hz por 2 segundos
            winsound.Beep(1000, 2000)
            break

        # Pausa o loop por 1 segundo antes de checar novamente
        time.sleep(1)


# Defina o seu alarme aqui (formato 24h: HH:MM)
alarme_usuario = "15:05"
despertar(alarme_usuario)
