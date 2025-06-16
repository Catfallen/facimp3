import serial
import time
import paho.mqtt.client as mqtt

BROKER = "192.168.0.109"
PORT = 1890
TOPIC_VEZ = "semaforo/vez"
QOS = 1
PORTA_SERIAL = '/dev/ttyACM0'
BAUDRATE = 9600

# Conecta ao broker MQTT
client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.loop_start()

# Conecta à porta serial do Arduino
arduino = serial.Serial(PORTA_SERIAL, BAUDRATE, timeout=1)

try:
    while True:
        if arduino.in_waiting > 0:
            msg = arduino.readline().decode().strip()
            if msg:
                print(f"Recebido do Arduino: {msg}")
                # Publica no tópico semaforo/vez
                client.publish(TOPIC_VEZ, msg, qos=QOS)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Encerrando...")

finally:
    client.loop_stop()
    arduino.close()
