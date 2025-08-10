from machine import Pin
import time

# Configuración de pines GPIO para LEDs
blancos = Pin(6, Pin.OUT)
verdes = Pin(27, Pin.OUT)
rojos = Pin(26, Pin.OUT)

# Función para parpadear LED blanco 2 veces
def leds_blancos():
    for _ in range(2):
        blancos.value(1)
        time.sleep(0.5)
        blancos.value(0)
        time.sleep(0.5)

# Función para parpadear LED verde 3 veces
def leds_verdes():
    for _ in range(3):
        verdes.value(1)
        time.sleep(0.5)
        verdes.value(0)
        time.sleep(0.5)

# Función para parpadear LED rojo 4 veces
def leds_rojos():
    for _ in range(4):
        rojos.value(1)
        time.sleep(0.5)
        rojos.value(0)
        time.sleep(0.5)

# Bucle principal que ejecuta la secuencia indefinidamente
while True:
    leds_blancos()
    leds_verdes()
    leds_rojos()
