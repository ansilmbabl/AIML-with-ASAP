// C++ code
//
int buz =9;
void setup()
{
  pinMode(buz, OUTPUT);
}

void loop()
{
  digitalWrite(buz, HIGH);
  delay(500);
  digitalWrite(buz, LOW);
  delay(250);
}
