import tkinter as tk
import paho.mqtt.client as mqtt

BROKER = "192.168.0.112"
PORT = 1891
TOPIC_VEZ = "semaforo/vez"
QOS = 1

class SemaforoCliente:
    def __init__(self, root, nome):
        self.root = root
        self.nome = nome  # "A" ou "B"

        self.cores = ["green", "yellow", "red"]
        self.indice_cor = 0
        self.ciclo_ativo = False

        # Label texto
        self.label = tk.Label(root, text=f"Cliente {self.nome} parado", font=("Arial", 20))
        self.label.pack(pady=10)

        # Canvas para desenhar o semáforo
        self.canvas = tk.Canvas(root, width=100, height=260, bg="black")
        self.canvas.pack(pady=10)

        # Coordenadas para os círculos (3 luzes)
        self.circulos = []
        raio = 30
        espacamento = 20
        inicio_y = 20
        cores_inativas = "gray20"

        for i in range(3):
            x0 = 50 - raio
            y0 = inicio_y + i * (raio * 2 + espacamento)
            x1 = 50 + raio
            y1 = y0 + raio * 2
            c = self.canvas.create_oval(x0, y0, x1, y1, fill=cores_inativas, outline="white", width=2)
            self.circulos.append(c)

        # MQTT client
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(BROKER, PORT)
        self.client.loop_start()

        # Começa com vermelho aceso no início
        self.apagar_todas_luzes()
        self.acender_luz("red")

    def on_connect(self, client, userdata, flags, rc):
        print(f"Cliente {self.nome} conectado com código {rc}")
        client.subscribe(TOPIC_VEZ, qos=QOS)

    def on_message(self, client, userdata, msg):
        mensagem = msg.payload.decode()
        print(f"Cliente {self.nome} recebeu mensagem: {mensagem}")
        if mensagem == self.nome:
            self.ciclo_ativo = True
            self.indice_cor = 0
            self.label.config(text=f"Cliente {self.nome} ativo", fg="white")
            self.ciclo_cores()
        else:
            self.ciclo_ativo = False
            self.label.config(text=f"Cliente {self.nome} parado", fg="red")
            # Enquanto parado, só vermelho aceso
            self.apagar_todas_luzes()
            self.acender_luz("red")

    def ciclo_cores(self):
        if not self.ciclo_ativo:
            return

        # Apaga todas as luzes
        self.apagar_todas_luzes()

        # Acende a luz atual
        cor_atual = self.cores[self.indice_cor]
        self.acender_luz(cor_atual)

        # Atualiza label para mostrar a cor atual
        self.label.config(text=f"Cliente {self.nome}: {cor_atual.upper()}", fg=cor_atual)

        self.indice_cor += 1
        if self.indice_cor >= len(self.cores):
            outro = "B" if self.nome == "A" else "A"
            print(f"Cliente {self.nome} terminou ciclo, passando para {outro}")
            self.client.publish(TOPIC_VEZ, outro, qos=QOS, retain=True)
            self.ciclo_ativo = False
    
            # Acende só o vermelho
            self.apagar_todas_luzes()
            self.acender_luz("red")
    
            self.label.config(text=f"Cliente {self.nome} parado", fg="red")
            return

        self.root.after(3000, self.ciclo_cores)

    def apagar_todas_luzes(self):
        for c in self.circulos:
            self.canvas.itemconfig(c, fill="gray20")

    def acender_luz(self, cor):
        # Mapeia cor para o círculo correspondente e pinta de forma brilhante
        index = self.cores.index(cor)
        self.canvas.itemconfig(self.circulos[index], fill=cor)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Semáforo MQTT")
    nome_cliente = input("Digite A ou B para identificar este cliente: ").strip().upper()
    if nome_cliente not in ["A", "B"]:
        print("Cliente inválido, digite A ou B")
        exit(1)

    app = SemaforoCliente(root, nome_cliente)

    # Cliente A inicia a vez dele
    if nome_cliente == "A":
        app.client.publish(TOPIC_VEZ, "A", qos=QOS, retain=True)

    root.mainloop()