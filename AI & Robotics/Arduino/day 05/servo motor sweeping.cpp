// C++ code
//

#include <Servo.h>
Servo myservo;
int position = 0;

void setup()
{
  myservo.attach(5);
}

void loop()
{
  for (position = 0; position <=180 ; position +=1)
  {
    myservo.write(position);
    delay(20);
  }
  for (position = 180; position >=0 ; position -=1)
  {
    myservo.write(position);
    delay(20);
  }
}
