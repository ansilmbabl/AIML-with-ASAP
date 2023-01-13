// C++ code
//
#include <Servo.h>
Servo servo1;

int trig = 12;
int echo = 11;
int duration;
int distance;

void setup()
{
  servo1.attach(5);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(trig,LOW); 
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  
  duration = pulseIn(echo,HIGH);
  distance = duration * 0.034/2 ;
  Serial.print("distance: "); 
  Serial.println(distance);
  
  if (distance < 50)
  {
    servo1.write(0);
    delay(1000);
    servo1.write(180);
    delay(1000);
  }
  else
  {
    servo1.write(90);
    delay(500);
  }
}
