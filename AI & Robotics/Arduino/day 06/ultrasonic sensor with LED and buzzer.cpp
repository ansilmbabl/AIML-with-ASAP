// C++ code
//

int trig = 11;
int echo = 9;
int distance;
int duration;

int led = 3;
int buzzer = 10;

void setup()
{
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  Serial.begin(9600);
  
  pinMode(led,OUTPUT);
  pinMode(buzzer,OUTPUT);
  
}

void loop()
{
  //creating waveform
  digitalWrite(trig,LOW); 
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  
  //getting input from echo
  duration = pulseIn(echo,HIGH); //duration of wave (micro seconds)
  distance = duration * 0.034/2 ; //distance of object in cm
  Serial.print("distance: "); 
  Serial.println(distance);
  
  if (distance > 50)
  {
    digitalWrite(led,HIGH);
      digitalWrite(buzzer,HIGH);
  }
  else
  {
    digitalWrite(led,LOW);
      digitalWrite(buzzer,LOW);
  }
}
