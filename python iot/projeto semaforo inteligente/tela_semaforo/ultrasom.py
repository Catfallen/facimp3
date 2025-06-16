import serial
import time
import paho.mqtt.client as mqtt

BROKER = "192.168.0.109"
PORT = 1890
TOPIC_ENVIO = "semaforo/vez"
TOPIC_CONFIRMACAO = "semaforo/pedestre"
QOS = 1

PORTA_SERIAL = '/dev/ttyACM0'
BAUDRATE = 9600

client = mqtt.Client(client_id="python-ultrasom")

def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Conectado ao broker com código: {rc}")
    if rc == 0:
        client.subscribe(TOPIC_CONFIRMACAO, qos=QOS)
        print(f"[MQTT] Inscrito no tópico: {TOPIC_CONFIRMACAO}")
    else:
        print("[MQTT] Falha na conexão.")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"[MQTT] Mensagem recebida no tópico '{msg.topic}': {payload}")
    if payload.strip() == "OK":
        arduino.write(b"OK\n")
        print("[Serial] OK enviado para o Arduino.")

client.on_connect = on_connect
client.on_message = on_message

print("[MQTT] Conectando ao broker...")
client.connect(BROKER, PORT, 60)
client.loop_start()

print(f"[Serial] Conectando na porta {PORTA_SERIAL}...")
try:
    arduino = serial.Serial(PORTA_SERIAL, BAUDRATE, timeout=1)
    time.sleep(2)
    print("[Serial] Conectado com sucesso.")
except Exception as e:
    print(f"[Erro Serial] {e}")
    exit()

print("[Sistema] Aguardando dados do Arduino...")

try:
    while True:
        if arduino.in_waiting > 0:
            msg = arduino.readline().decode().strip()
            if msg:
                print(f"[Serial] Recebido do Arduino: {msg}")
                client.publish(TOPIC_ENVIO, msg, qos=QOS)
                print(f"[MQTT] Publicado '{msg}' no tópico {TOPIC_ENVIO}")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n[Encerrando] Ctrl+C detectado.")

finally:
    client.loop_stop()
    arduino.close()
    print("[Sistema] Finalizado com segurança.")