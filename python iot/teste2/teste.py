import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado: " + str(rc))
    client.subscribe("temperatura")

# Função de callback quando uma mensagem é recebida
def on_message(client, userdata, msg):
    print(f"Mensagem recebida: {msg.payload.decode()}")
    try:
        temperatura = int(msg.payload.decode())
        if temperatura >= 50:
            print("Temperatura acima")
        else:
            print("Temperatura abaixo")
    except:
        print("dado invalido")
# Cria um cliente MQTT
client = mqtt.Client()

# Define as funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Conecta ao broker Mosquitto local
client.connect("localhost", 1883, 60)

# Inicia o loop para manter o subscriber ativo
client.loop_start()

#Aguarda um tempo para ver se as mensagens são recebidas
import time
while True:
    pass

# Para o loop após o teste
client.loop_stop()
