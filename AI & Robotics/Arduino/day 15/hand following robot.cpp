// C++ code
//
int ml1 = 10;
int ml2 = 11;
int mr1 = 6;
int mr2 = 9;

int en12 = 3;
int en34 = 5;

int trig =12;
int echo =13;

long time,distance;

void setup()
{
  pinMode(ml1, OUTPUT);
  pinMode(ml2, OUTPUT);
  pinMode(mr1, OUTPUT);
  pinMode(mr2, OUTPUT);
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
}
void loop()
{
  sensor();
  puppy();
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

void backward()
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, HIGH);
  digitalWrite(mr1, LOW);
  digitalWrite(mr2, HIGH);
  analogWrite(en12, 200);
  analogWrite(en34, 200);
}

void left()
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, HIGH);
  digitalWrite(mr1, HIGH);
  digitalWrite(mr2, LOW);
  analogWrite(en12, 200);
  analogWrite(en34, 200);
}

void right()
{
  digitalWrite(ml1, HIGH);
  digitalWrite(ml2, LOW);
  digitalWrite(mr1, LOW);
  digitalWrite(mr2, HIGH);
  analogWrite(en12, 200);
  analogWrite(en34, 200);
}

void stop()
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, LOW);
  digitalWrite(mr1, LOW);
  digitalWrite(mr2, LOW);
  analogWrite(en12, 200);
  analogWrite(en34, 200);
}

void sensor()
{
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(2);
  digitalWrite(trig, LOW);
  
  time = pulseIn(echo, HIGH);
  distance = time * .034/2;
  Serial.println(distance);
}

void puppy()
{
  if(distance <50 && distance >20)                       
  {
    forward();
    Serial.println("coming towards.....");
  }
  else if(distance > 0 && distance <15)
  {
    backward();
    Serial.println("Going away.....");
  }
  else
  {
    stop();
    Serial.println("stuck there...");
  }
}
