// C++ code

int ml1 = 9;
int ml2 = 11;
int mr1 = 2;
int mr2 = 5;

void setup()
{
  pinMode(ml1, OUTPUT);
  pinMode(ml2, OUTPUT);
  pinMode(mr1, OUTPUT);
  pinMode(mr2, OUTPUT);
}

void loop()
{
  forward();
    delay(2000);
  stop();
    delay(2000);
  backward();
    delay(2000);
  stop();
    delay(2000);
  left();
    delay(2000);
  stop();
    delay(2000);
  right();
    delay(2000);
  stop();
    delay(2000);
}

void forward()
{
  digitalWrite(ml1, HIGH);
  digitalWrite(ml2, LOW);
  digitalWrite(mr1, HIGH);
  digitalWrite(mr2, LOW);
}

void backward()
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, HIGH);
  digitalWrite(mr1, LOW);
  digitalWrite(mr2, HIGH);
}

void stop()
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, LOW);
  digitalWrite(mr1, LOW);
  digitalWrite(mr2, LOW);
}

void left()
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, HIGH);
  digitalWrite(mr1, HIGH);
  digitalWrite(mr2, LOW);
}

void right()
{
  digitalWrite(ml1, HIGH);
  digitalWrite(ml2, LOW);
  digitalWrite(mr1, LOW);
  digitalWrite(mr2, HIGH);
}
