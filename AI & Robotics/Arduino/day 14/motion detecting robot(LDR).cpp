int ml1 = 4;
int ml2 = 5;
int mr1 = 6;
int mr2 = 7;

int en12 = 2;
int en34 = 3;

int ldr = A2;
int ldr_value;
int mot_sp;

void setup()
{
  pinMode(ml1, OUTPUT);
  pinMode(ml2, OUTPUT);
  pinMode(mr1, OUTPUT);
  pinMode(mr2, OUTPUT);
  pinMode(en12, OUTPUT);
  pinMode(en34, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  ld();
}

void forward()
{
  digitalWrite(ml1, HIGH);
  digitalWrite(ml2, LOW);
  digitalWrite(mr1, HIGH);
  digitalWrite(mr2, LOW);
  analogWrite(en12, 200);
  analogWrite(en34, 200);
}

void stop()
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, LOW);
  digitalWrite(mr1, LOW);
  digitalWrite(mr2, LOW);
}

void ld()
{
  mot_sp = digitalRead(ml1);
  ldr_value = analogRead(ldr);
  Serial.println(ldr_value);
  Serial.println(mot_sp);
  if (ldr_value > 400)
  {
    forward();
  }
  else
  {
    stop();
  }
}
    
