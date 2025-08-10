from machine import Pin
import time

# Configuración de pines GPIO para LEDs
blancos = Pin(6, Pin.OUT)
verdes = Pin(27, Pin.OUT)
rojos = Pin(26, Pin.OUT)

# Parpadeo LED blanco 2 veces
for _ in range(2):
    blancos.value(1)  # Enciende LED blanco
    time.sleep(0.5)
    blancos.value(0)  # Apaga LED blanco
    time.sleep(0.5)

# Parpadeo LED verde 3 veces
for _ in range(3):
    verdes.value(1)  # Enciende LED verde
    time.sleep(0.5)
    verdes.value(0)  # Apaga LED verde
    time.sleep(0.5)

# Parpadeo LED rojo 4 veces
for _ in range(4):
    rojos.value(1)  # Enciende LED rojo
    time.sleep(0.5)
    rojos.value(0)  # Apaga LED rojo
    time.sleep(0.5)
