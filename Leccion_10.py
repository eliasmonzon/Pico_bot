from machine import Pin
import time

# --- Configuración de pines ---
trig = Pin(7, Pin.OUT)
echo = Pin(8, Pin.IN)

blancos = Pin(6, Pin.OUT)
verdes = Pin(27, Pin.OUT)
rojas = Pin(26, Pin.OUT)

motorA1 = Pin(18, Pin.OUT)
motorA2 = Pin(19, Pin.OUT)
motorB1 = Pin(20, Pin.OUT)
motorB2 = Pin(21, Pin.OUT)

# --- Función del sensor ultrasónico ---
def ultrasonico_sensor():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    start_time = 0
    end_time = 0

    timeout = time.ticks_us() + 30000
    while echo.value() == 0 and time.ticks_us() < timeout:
        start_time = time.ticks_us()

    timeout = time.ticks_us() + 30000
    while echo.value() == 1 and time.ticks_us() < timeout:
        end_time = time.ticks_us()

    pulse_duration = time.ticks_diff(end_time, start_time)
    distance = (pulse_duration * 0.0343) / 2

    print("Distancia:", distance, "cm")
    time.sleep(0.1)

    return distance < 20 and distance > 0

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
    motorB1.low()
    motorB2.high()

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
        time.sleep(0.5)
        atras()
        time.sleep(0.5)
        parar()
        time.sleep(0.5)
        derecha()
        time.sleep(0.5)
        parar()
        time.sleep(0.5)
    else:
        adelante()

