// Semáforo
int ledVerde = 2;
int ledAmarelo = 3;
int ledVermelho = 4;

// Sensor ultrassônico com pino SIG
int sig = 5;
int buzzer = 8;
void setup() {
  Serial.begin(9600);

  pinMode(ledVerde, OUTPUT);
  pinMode(ledAmarelo, OUTPUT);
  pinMode(ledVermelho, OUTPUT);

  pinMode(sig, OUTPUT);
}

void loop() {
  long duracao;
  int distancia;
  tone(buzzer, 1000); // 1000 Hz → som agudo
  delay(500);
  
  // Envia pulso
  pinMode(sig, OUTPUT);
  digitalWrite(sig, LOW);
  delayMicroseconds(2);
  digitalWrite(sig, HIGH);
  delayMicroseconds(10);
  digitalWrite(sig, LOW);

  // Lê retorno
  pinMode(sig, INPUT);
  duracao = pulseIn(sig, HIGH);

  // Calcula distância em cm
  distancia = duracao * 0.034 / 2;

  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");

  if (distancia < 20) { // Objeto detectado próximo
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledAmarelo, HIGH);
    delay(1000);
    digitalWrite(ledAmarelo, LOW);
    digitalWrite(ledVermelho, HIGH);
    delay(3000);
    digitalWrite(ledVermelho, LOW);
    digitalWrite(ledVerde, HIGH);
  } else { // Livre
    digitalWrite(ledVermelho, LOW);
    digitalWrite(ledAmarelo, LOW);
    digitalWrite(ledVerde, HIGH);
  }

  delay(500);
  noTone(buzzer);      // Para o som
  delay(5000);

}
