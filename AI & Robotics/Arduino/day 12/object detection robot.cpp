// C++ code

int ml1 = 9;
int ml2 = 11;
int mr1 = 2;
int mr2 = 5;

int trig = 4;
int echo = 7;

int en12 = 6;
int en34 = 3;

long distance,duration;

void setup()
{
  pinMode(ml1, OUTPUT);
  pinMode(ml2, OUTPUT);
  pinMode(mr1, OUTPUT);
  pinMode(mr2, OUTPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(en12, OUTPUT);
  pinMode(en34, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  forward();
  sensor();
  sens();
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

void sensor()
{
  digitalWrite(trig,LOW);
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  
  duration = pulseIn(echo, HIGH);
  distance = duration * 0.034/2 ;
  Serial.print("distance: "); 
  Serial.println(distance);
}

void sens()
{
  if (distance <50)
  {
    stop();
    delay(2000);
  }
}
