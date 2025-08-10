from machine import Pin
import utime

# --- Configuración de pines ---

# Sensor ultrasónico
trig = Pin(7, Pin.OUT)
echo = Pin(8, Pin.IN)

# LEDs indicadores
blancos = Pin(6, Pin.OUT)
verdes = Pin(27, Pin.OUT)
rojas = Pin(26, Pin.OUT)

# Motores
motorA1 = Pin(18, Pin.OUT)
motorA2 = Pin(19, Pin.OUT)
motorB1 = Pin(20, Pin.OUT)
motorB2 = Pin(21, Pin.OUT)

# --- Función del sensor ultrasónico ---
def ultrasonico_sensor():
    """Mide la distancia y devuelve True si hay un obstáculo a menos de 20 cm."""
    trig.value(0)
    utime.sleep_us(2)  # Asegura que trig está bajo
    trig.value(1)
    utime.sleep_us(10)
    trig.value(0)

    while echo.value() == 0:
        start_time = utime.ticks_us()
    while echo.value() == 1:
        end_time = utime.ticks_us()

    pulse_duration = utime.ticks_diff(end_time, start_time)
    distance = (pulse_duration * 0.0343) / 2
    print("Distancia:", distance, "cm")
    utime.sleep(0.1)

    return distance < 20

# --- Funciones de movimiento ---
def adelante():
    rojas.value(0)
    blancos.value(1)
    verdes.value(1)
    motorA1.high()
    motorA2.low()
    motorB1.low()
    motorB2.high()

def atras():
    motorA1.low()
    motorA2.high()
    motorB1.high()
    motorB2.low()

def derecha():
    motorA1.high()
    motorA2.low()
    motorB1.high()
    motorB2.low()

def parar():
    rojas.value(1)
    blancos.value(0)
    verdes.value(0)
    motorA1.low()
    motorA2.low()
    motorB1.low()
    motorB2.low()

# --- Bucle principal ---
while True:
    if ultrasonico_sensor():
        parar()
        utime.sleep(0.5)
        atras()
        utime.sleep(0.5)
        parar()
        utime.sleep(0.5)
        derecha()
        utime.sleep(0.5)
        parar()
        utime.sleep(0.5)
    else:
        adelante()
