from machine import Pin, PWM
import time

# Configuración del buzzer en el pin GPIO 22
buzzer = PWM(Pin(22))

while True:
    # Frecuencia alta
    buzzer.freq(1000)
    buzzer.duty_u16(10000)
    time.sleep(0.3)

    # Frecuencia baja
    buzzer.freq(600)
    buzzer.duty_u16(10000)
    time.sleep(0.3)

    # Silencio
    buzzer.duty_u16(0)
    time.sleep(0.1)
