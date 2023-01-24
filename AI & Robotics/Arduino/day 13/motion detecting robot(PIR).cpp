
int ml1 = 4;
int ml2 = 5;
int mr1 = 7;
int mr2 = 8;
int en12 = 3;
int en34 = 6;

int PIR = 9;
int PIR_stat;

void setup()
{
  pinMode(ml1,OUTPUT);
  pinMode(ml2,OUTPUT);
  pinMode(mr1,OUTPUT);
  pinMode(mr2,OUTPUT);
  pinMode(en12,OUTPUT);
  pinMode(en34,OUTPUT);
  pinMode(PIR,INPUT);
  Serial.begin(9600);
}

void loop()
{
  det();
}

void forward()
{
  digitalWrite(ml1,HIGH);
  digitalWrite(ml2,LOW);
  digitalWrite(mr1,HIGH);
  digitalWrite(mr2,LOW);
  analogWrite(en12,200);
  analogWrite(en34,200);
}

void stop()
{
  digitalWrite(ml1,LOW);
  digitalWrite(ml2,LOW);
  digitalWrite(mr1,LOW);
  digitalWrite(mr2,LOW);
}

void left()
{
  digitalWrite(ml1,LOW);
  digitalWrite(ml2,HIGH);
  digitalWrite(mr1,HIGH);
  digitalWrite(mr2,LOW);
  analogWrite(en12,200);
  analogWrite(en34,200);
} 

void right()
{
  digitalWrite(ml1,HIGH);
  digitalWrite(ml2,LOW);
  digitalWrite(mr1,LOW);
  digitalWrite(mr2,HIGH);
  analogWrite(en12,200);
  analogWrite(en34,200);
} 

void det()
{
  PIR_stat = digitalRead(PIR);
 if (PIR_stat == HIGH)
 {
   stop();
   Serial.println("obstacle........");
   left();
   Serial.println("taking left turn...");
   delay(1000);
 }
 else
  {
    forward();
   	Serial.println("Going forward...");
  }
}
