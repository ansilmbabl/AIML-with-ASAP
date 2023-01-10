// C++ code
//

int button_state;
int button = 5;

void setup()
{
  Serial.begin(9600);
  pinMode(button,INPUT);
}

void loop()
{
  button_state = digitalRead(button);
  Serial.println(button_state);
  //or
  //Serial.println(digitalRead(button));
}
