from machine import UART, Pin, PWM
import time, _thread

# Comunicación Bluetooth (UART0)
modulo = UART(0, 9600, tx=Pin(16), rx=Pin(17))

# Pines de sensores, motores, LEDs y buzzer
trig = Pin(7, Pin.OUT)
echo = Pin(8, Pin.IN)
motora1 = Pin(18, Pin.OUT)
motora2 = Pin(19, Pin.OUT)
motorb1 = Pin(20, Pin.OUT)
motorb2 = Pin(21, Pin.OUT)
blancas = Pin(6, Pin.OUT)
verdes = Pin(27, Pin.OUT)
rojas = Pin(26, Pin.OUT)
buzzer = PWM(Pin(22))

# Funciones de movimiento
def atras():
    motora1.high()
    motora2.low()
    motorb1.low()
    motorb2.high()

def adelante():
    motora1.low()
    motora2.high()
    motorb1.high()
    motorb2.low()

def derecha():
    motora1.low()
    motora2.high()
    motorb1.low()
    motorb2.high()

def izquierda():
    motora1.high()
    motora2.low()
    motorb1.high()
    motorb2.low()

def parar():
    motora1.low()
    motora2.low()
    motorb1.low()
    motorb2.low()
    rojas.value(1)
    time.sleep(0.3)
    rojas.value(0)

# Funciones auxiliares
def bncs():
    blancas.value(1)

def ver():
    verdes.value(1)

def bocina():
    buzzer.freq(500)
    buzzer.duty_u16(10000)

def detecta():
    parar()
    bocina()
    bncs()
    time.sleep(0.3)
    blancas.value(0)
    rojas.value(0)
    buzzer.duty_u16(0)

# Melodía de inicio
def inicio():
    def playNote(frequency, duration, pause):
        buzzer.duty_u16(10000)
        buzzer.freq(frequency)
        time.sleep(duration)
        buzzer.duty_u16(0)
        time.sleep(pause)

    notes = [440, 494, 523, 587, 659, 698, 784]
    for note in notes:
        playNote(note, 0.1, 0.1)
        for led in [blancas, verdes, rojas]:
            led.value(1)
            time.sleep(0.02)
            led.value(0)

# Sensor ultrasónico con timeout
def ultrasonido():
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()

    start = time.ticks_us()
    while echo.value() == 0:
        if time.ticks_diff(time.ticks_us(), start) > 30000:
            return 999  # sin respuesta
        pulse_start = time.ticks_us()

    while echo.value() == 1:
        if time.ticks_diff(time.ticks_us(), start) > 30000:
            return 999
        pulse_end = time.ticks_us()

    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    return (pulse_duration * 0.0343) / 2

# Ejecutar la melodía de inicio en el segundo núcleo
_thread.start_new_thread(inicio, ())

# Bucle principal
dato = ""
while True:
    if modulo.any() > 0:
        recibido = modulo.read(1)
        if recibido:
            dato = recibido.decode().strip()
            print("Dato recibido:", dato)
            if dato == "F":
                adelante()
            elif dato == "B":
                atras()
            elif dato == "R":
                izquierda()
            elif dato == "L":
                derecha()
            elif dato == "S":
                parar()
            elif dato == "W":
                bncs()
            elif dato == "w":
                blancas.value(0)
            elif dato == "U":
                ver()
            elif dato == "u":
                verdes.value(0)
            elif dato == "X":
                inicio()
            elif dato == "V":
                bocina()
            elif dato == "v":
                buzzer.duty_u16(0)

    # Verificar obstáculo
    distancia_actual = ultrasonido()
    if distancia_actual < 15 and dato == "F":
        detecta()
