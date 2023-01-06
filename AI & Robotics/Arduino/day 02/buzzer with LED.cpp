// C++ code
//
int red=13;
int yellow=9;
int green=5;
int buzzer=2;

void setup()
{
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop()
{
  digitalWrite(red, HIGH);
  digitalWrite(buzzer, HIGH);
  delay(500); 
  digitalWrite(red, LOW);
  digitalWrite(buzzer, LOW);
  delay(750);
  
  digitalWrite(yellow, HIGH);
  digitalWrite(buzzer, HIGH);
  delay(500); 
  digitalWrite(yellow, LOW);
  digitalWrite(buzzer, LOW);
  delay(750);
  
  digitalWrite(green, HIGH);
  digitalWrite(buzzer, HIGH);
  delay(500); 
  digitalWrite(green, LOW);
  digitalWrite(buzzer, LOW);
  delay(750);
}
