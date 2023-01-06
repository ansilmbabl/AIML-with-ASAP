// C++ code
//

int red=13;
int yellow=11;
int green=9;
void setup()
{
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
}

void loop()
{
  digitalWrite(red, HIGH);
  delay(250); 
  digitalWrite(red, LOW);
  delay(500);
  
  digitalWrite(yellow, HIGH);
  delay(250); 
  digitalWrite(yellow, LOW);
  delay(500);
  
  digitalWrite(green, HIGH);
  delay(250); 
  digitalWrite(green, LOW);
  delay(500);
}
