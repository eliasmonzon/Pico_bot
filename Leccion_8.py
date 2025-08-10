from machine import Pin, PWM
import time

# Configuración del buzzer y los LEDs
buzzer = PWM(Pin(22))
blancos = Pin(6, Pin.OUT)
verdes = Pin(27, Pin.OUT)
rojos = Pin(26, Pin.OUT)

# Diccionario de notas con frecuencias (Hz)
notas = {
    'Do': 261, 'Do*': 523, 'Re': 293, 'Re*': 587, 'Mi': 329, 'Mi*': 659,
    'Fa': 349, 'Fa*': 698, 'Sol': 392, 'Sol*': 784, 'La': 440, 'La*': 880,
    'Si': 493, 'Sib': 466, 'Sol#': 831, 'Re#': 622, 'Fa#': 740, 'La#': 932,
    'Silencio': 0
}

# Melodía de Jingle Bells
melodia = [
    ('Mi', 0.3), ('Mi', 0.3), ('Mi', 0.6),
    ('Mi', 0.3), ('Mi', 0.3), ('Mi', 0.6),
    ('Mi', 0.3), ('Sol', 0.3), ('Do', 0.3), ('Re', 0.3), ('Mi', 0.6),
    ('Fa', 0.3), ('Fa', 0.3), ('Fa', 0.3), ('Fa', 0.3),
    ('Fa', 0.3), ('Mi', 0.3), ('Mi', 0.3), ('Mi', 0.3), ('Mi', 0.3),
    ('Mi', 0.3), ('Re', 0.3), ('Re', 0.3), ('Mi', 0.3), ('Re', 0.6),
    ('Sol', 0.6),
    ('Mi', 0.3), ('Mi', 0.3), ('Mi', 0.6),
    ('Mi', 0.3), ('Sol', 0.3), ('Do', 0.3), ('Re', 0.3), ('Mi', 0.6),
    ('Sol', 0.3), ('Sol', 0.3), ('Fa', 0.3), ('Re', 0.3), ('Do', 0.6)
]

# Función que reproduce una nota con luces sincronizadas
def reproducir_nota_con_luces(nota, duracion):
    if nota in notas:
        frecuencia = notas[nota]

        # Encender LED blanco
        blancos.value(1)
        verdes.value(0)
        rojos.value(0)

        if frecuencia == 0:
            buzzer.duty_u16(0)  # Silencio
        else:
            buzzer.freq(frecuencia)
            buzzer.duty_u16(10000)

        time.sleep(duracion / 3)

        # Encender LED verde
        blancos.value(0)
        verdes.value(1)
        time.sleep(duracion / 3)

        # Encender LED rojo
        verdes.value(0)
        rojos.value(1)
        time.sleep(duracion / 3)

        # Apagar buzzer y LEDs
        buzzer.duty_u16(0)
        rojos.value(0)
        time.sleep(0.05)
    else:
        print(f'Nota "{nota}" no definida.')

# Bucle principal
while True:
    for nota, duracion in melodia:
        reproducir_nota_con_luces(nota, duracion)
    time.sleep(2)  # Espera entre repeticiones
