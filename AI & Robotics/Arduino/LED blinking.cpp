// C++ code
//

int ledpin = 13;
void setup()
{
  pinMode(ledpin, OUTPUT);
}

void loop()
{
  digitalWrite(ledpin, HIGH);
  delay(500); // Wait for 500 millisecond(s)
  digitalWrite(ledpin, LOW);
  delay(500); // Wait for 500 millisecond(s)
}
