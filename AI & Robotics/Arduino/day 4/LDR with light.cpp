// C++ code
//
int ldr = A5;
int ldr_value;
int led = 3;
int buzzer = 7;

void setup()
{
  Serial.begin(9600);
  pinMode(led,OUTPUT);
  pinMode(buzzer,OUTPUT);
}

void loop()
{
  ldr_value = analogRead(ldr);
  Serial.println(ldr_value);
  
  if (ldr_value <= 300){
    digitalWrite(led,HIGH);
      digitalWrite(buzzer,HIGH);
  }
  else{
    digitalWrite(led,LOW);
      digitalWrite(buzzer,LOW);
  }
}
