from machine import Pin, PWM
import time

# Configuración del buzzer
buzzer = PWM(Pin(22))

# Diccionario de notas musicales
notas = {
    'Do': 261, 'Do*': 523, 'Re': 293, 'Re*': 587, 'Mi': 329, 'Mi*': 659,
    'Fa': 349, 'Fa*': 698, 'Sol': 392, 'Sol*': 784, 'La': 440, 'La*': 880,
    'Si': 493, 'Sib': 466, 'Sol#': 831, 'Re#': 622, 'Fa#': 740, 'La#': 932,
    'Silencio': 0
}

# Melodía: lista de tuplas (nota, duración en segundos)
melodia = [
    ('Mi*', 0.15), ('Mi*', 0.15), ('Silencio', 0.1), ('Mi*', 0.15),
    ('Silencio', 0.1), ('Do*', 0.15), ('Mi*', 0.15), ('Sol*', 0.3),
    ('Silencio', 0.3), ('Sol', 0.3), ('Silencio', 0.3),
    ('Do*', 0.15), ('Silencio', 0.1), ('Sol', 0.15), ('Mi', 0.15),
    ('La', 0.15), ('Si', 0.15), ('Sib', 0.15), ('La', 0.15),
    ('Sol*', 0.15), ('Mi*', 0.15), ('Sol*', 0.15), ('La*', 0.3),
    ('Fa*', 0.15), ('Sol*', 0.15), ('Mi*', 0.15), ('Do*', 0.15),
    ('Re', 0.15), ('Si', 0.15)
]

# Función que reproduce una nota
def reproducir_nota(nota, duracion):
    if nota in notas:
        frecuencia = notas[nota]
        if frecuencia == 0:
            buzzer.duty_u16(0)  # Silencio
        else:
            buzzer.freq(frecuencia)
            buzzer.duty_u16(10000)
        time.sleep(duracion)
        buzzer.duty_u16(0)
        time.sleep(0.05)
    else:
        print(f'Nota "{nota}" no definida.')

# Reproduce la melodía en bucle
while True:
    for nota, duracion in melodia:
        reproducir_nota(nota, duracion)
    time.sleep(1)
