import datetime
import threading
import time
import winsound
input threading

def despertar(hora_alarme):
    print(f"Alarme configurado para as {hora_alarme}")


senha = ''
hora_alarme = "00:00"
hora = int(input('Digite a hora q deseja acordar: '))
minuto = int(input('Digite o minuto q deseja acordar: '))
# Faz com q seja incuido o 0 antes do minuto para q seja formatado e encontre o horario certo
if minuto < 10:
    minuto = str(f'0{minuto}')
alarme_usuario = str(f'{hora}:{minuto}')
despertar(alarme_usuario)
hora_alarme = alarme_usuario
while True:
        # Pega o horário atual e formata para Hora:Minuto
    agora = datetime.datetime.now().strftime("%H:%M")

        # Compara a hora atual com a hora do alarme
    if agora == hora_alarme:
        print("Hora de acordar! Beep! Beep!")
        while True:
                # Emite um bipe de 1000Hz por 2 segundos
            winsound.Beep(1050, 200)
            time.sleep(0.01)
            senha = str(input('Digite sua senha para para...'))
    if senha != 'TalineLindaMeuAmor':
        print('Houve um ERRO ao cadastrar o arquivo!')

        #Pausa o loop por 1 segundo antes de checar novamente
        time.sleep(1)
