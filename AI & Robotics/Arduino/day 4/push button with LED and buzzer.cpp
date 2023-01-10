// C++ code
//

int button_state;
int button = 3;
int led = 5;
int buzzer = 9;

void setup()
{
  Serial.begin(9600);
  pinMode(button,INPUT);
  pinMode(led,OUTPUT);
  pinMode(buzzer,OUTPUT);
  
}

void loop()
{
  button_state = digitalRead(button);
  Serial.println(button_state);
  
  if (button_state == 1){
    digitalWrite(led,HIGH);
      digitalWrite(buzzer,HIGH);
  }
  else{
    digitalWrite(led,LOW);
    digitalWrite(buzzer,LOW);
  }
  
}
