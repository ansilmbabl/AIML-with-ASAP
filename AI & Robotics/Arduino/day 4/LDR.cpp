// C++ code
//
int ldr = A5;
//int ldr2 = A0;
int ldr_value;
//int ldr_value2;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  ldr_value = analogRead(ldr);
  Serial.println(ldr_value);
  
  //ldr_value2 = analogRead(ldr2);
  //Serial.println(ldr_value2);
}
