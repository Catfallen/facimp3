void setup() {
  
  int red2 = 12;
  int yel2 = 11;
  int gre2 = 10;
  int r = 4;
  int y = 3;
  int v = 2;
  
  pinMode(r, OUTPUT); // LED vermelho
  pinMode(y, OUTPUT); // LED amarelo
  pinMode(v, OUTPUT); // LED verde
  pinMode(red2, OUTPUT);
  pinMode(yel2, OUTPUT);
  pinMode(gre2, OUTPUT);
  
  

}

void desligarTodos(int r, int y, int g) {
  digitalWrite(r, LOW);
  digitalWrite(y, LOW);
  digitalWrite(g, LOW);
}

void semaforo(int r, int y, int g) {
  desligarTodos(r, y, g);
  digitalWrite(g, HIGH);
  delay(2000);

  desligarTodos(r, y, g);
  digitalWrite(y, HIGH);
  delay(2000);

  desligarTodos(r, y, g);
  digitalWrite(r, HIGH);
  delay(2000);

  desligarTodos(r, y, g);
}

void stop(int r,int y,int g){
  digitalWrite(r, HIGH);
  digitalWrite(y, LOW);
  digitalWrite(g, LOW);  
}


void loop() {
  int sema1 = true;
  int sema2 = !sema1;
  
  
  int red2 = 12;
  int yel2 = 11;
  int gre2 = 10;
  int r = 4;
  int y = 3;
  int g = 2;
  
  while(true){
    if(sema1){
      stop(red2,yel2,gre2);
      semaforo(r,y,g);
      sema1 = !sema1;
      sema2 = !sema2;
    }else{
      stop(r,y,g);
      semaforo(red2,yel2,gre2);
      sema1 = !sema1;
      sema2 = !sema2;
    }
  }
}