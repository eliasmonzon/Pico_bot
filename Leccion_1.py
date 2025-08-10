import time
from machine import Pin

blancos = Pin(6, Pin.OUT)  # LED blancos en GPIO 6
verdes = Pin(27, Pin.OUT)  # LED verdes en GPIO 27
rojos = Pin(26, Pin.OUT)   # LED rojos en GPIO 26

while True:
    verdes.value(0)      # Apaga LEDs verdes
    blancos.value(1)     # Enciende LEDs blancos
    time.sleep(1)        # Espera 1 segundo

    blancos.value(0)     # Apaga LEDs blancos
    rojos.value(1)       # Enciende LEDs rojos
    time.sleep(1)        # Espera 1 segundo

    rojos.value(0)       # Apaga LEDs rojos
    verdes.value(1)      # Enciende LEDs verdes
    time.sleep(1)        # Espera 1 segundo antes de reiniciar el ciclo
