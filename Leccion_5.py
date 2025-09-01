from machine import Pin
import time

# Configuración del pin para el LED blanco
blancos = Pin(6, Pin.OUT)  # LED conectado al GPIO 6 configurado como salida

# Configuración del pin para el sensor LDR
modulo_ldr = Pin(15, Pin.IN)

while True:
    if modulo_ldr.value() == 0:  # Detecta luz "modulo envia 0 al gpio 15"
        blancos.value(0)         # Apaga el LED
    else:  # No detecta luz
        blancos.value(1)         # Enciende el LED
    time.sleep(0.1)              # Pequeña pausa para evitar lecturas muy rápidas


