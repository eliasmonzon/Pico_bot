from machine import Pin, PWM
import time
import _thread

# Configuración del buzzer
buzzer = PWM(Pin(22))

# Configuración de los LEDs
blancos = Pin(6, Pin.OUT)
verdes = Pin(27, Pin.OUT)
rojos = Pin(26, Pin.OUT)

# Diccionario de notas musicales
notas = {
    'Do': 261, 'Re': 293, 'Mi': 329, 'Fa': 349, 'Sol': 392,
    'La': 440, 'Si': 493, 'Do*': 523, 'Re*': 587, 'Mi*': 659,
    'Silencio': 0
}

# Melodía extendida (nota, duración en segundos)
melodia = [
    ('Do', 0.5), ('Re', 0.5), ('Mi', 0.5), ('Fa', 0.5),
    ('Sol', 0.5), ('La', 0.5), ('Si', 0.5), ('Do*', 0.5),
    ('Si', 0.5), ('La', 0.5), ('Sol', 0.5), ('Fa', 0.5),
    ('Mi', 0.5), ('Re', 0.5), ('Do', 0.5),
    ('Silencio', 0.5),
    ('Do', 0.25), ('Re', 0.25), ('Mi', 0.25), ('Re', 0.25),
    ('Do', 0.5), ('Sol', 0.5), ('Fa', 0.5), ('Mi', 0.5),
    ('Re', 0.5), ('Do', 0.5), ('Silencio', 0.5)
]

# Secuencia de luces (LED, duración en segundos)
luces = [
    (blancos, 0.5), (verdes, 0.5), (rojos, 0.5),
    (blancos, 0.25), (verdes, 0.25), (rojos, 0.25),
    (verdes, 0.5), (blancos, 0.5), (rojos, 0.5)
]

# Función para reproducir la melodía
def reproducir_melodia():
    while True:
        for nota, duracion in melodia:
            frecuencia = notas[nota]
            if frecuencia == 0:  # Silencio
                buzzer.duty_u16(0)
            else:
                buzzer.freq(frecuencia)
                buzzer.duty_u16(10000)
            time.sleep(duracion)
        buzzer.duty_u16(0)  # Apagar buzzer al final de la melodía
        time.sleep(1)

# Función para controlar las luces
def controlar_luces():
    while True:
        for led, duracion in luces:
            led.on()
            time.sleep(duracion)
            led.off()

# Ejecutar funciones en paralelo con los dos núcleos
_thread.start_new_thread(reproducir_melodia, ())  # Core 1
controlar_luces()  # Core 0
