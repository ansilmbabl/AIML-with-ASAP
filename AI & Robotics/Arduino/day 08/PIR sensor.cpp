// C++ code
//
#include <Servo.h>
Servo servo1;

int PIR = 10;
int PIR_stat;
int led = 3;
int buzzer = 5;

void setup()
{
  servo1.attach(2);
  pinMode(PIR, INPUT);
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  
  PIR_stat = digitalRead(PIR);
  if (PIR_stat == HIGH)
  {
    Serial.println("detected");
    digitalWrite(led,HIGH);
    digitalWrite(buzzer,HIGH);
    delay(1000);
    
    //servo1.write(0):
    //delay(1000);
    servo1.write(180);
    
  }
  else
  {
    Serial.println("not detected");
    digitalWrite(led,LOW);
    digitalWrite(buzzer,LOW);
    
    servo1.write(90);
    delay(1000);
  }
}
