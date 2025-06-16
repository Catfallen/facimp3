import serial
import time
import paho.mqtt.client as mqtt

BROKER = "172.16.9.39"
PORT = 1890
TOPIC_VEZ = "semaforo/vez"
QOS = 1

PORTA_SERIAL = '/dev/ttyACM0'
BAUDRATE = 9600

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Conectado com código {rc}")
    client.subscribe(TOPIC_VEZ, qos=QOS)

def on_message(client, userdata, msg):
    pass  # Não precisa agir aqui no ultrasom

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_start()

try:
    arduino = serial.Serial(PORTA_SERIAL, BAUDRATE, timeout=1)
    time.sleep(2)
    print("[Serial] Conectado no Arduino")
except Exception as e:
    print(f"[Erro Serial] {e}")
    exit()

vez_atual = None

while True:
    if arduino.in_waiting:
        linha = arduino.readline().decode().strip()
        if linha:
            print(f"[Serial] {linha}")

            if linha == "C":  # presença detectada: pausa o ciclo
                vez_atual = "C"
                client.publish(TOPIC_VEZ, "C", qos=QOS, retain=True)
                print("[MQTT] Publicado C - ciclo pausado")
            elif linha == "R":  # sem presença, libera ciclo
                if vez_atual == "C" or vez_atual is None:
                    vez_atual = "A"
                    client.publish(TOPIC_VEZ, "A", qos=QOS, retain=True)
                    print("[MQTT] Publicado A - iniciando ciclo")
            else:
                # Se Arduino enviar "A" ou "B" explicitamente, pode publicar
                if linha in ["A", "B"]:
                    vez_atual = linha
                    client.publish(TOPIC_VEZ, vez_atual, qos=QOS, retain=True)
                    print(f"[MQTT] Publicado {vez_atual}")

    time.sleep(0.1)