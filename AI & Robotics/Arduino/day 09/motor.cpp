// C++ code
//

int ml1 = 2; // input 2
int ml2 = 5; // input 1
int mr1 = 8; 
int mr2 = 10;

void setup()
{
  pinMode(ml1, OUTPUT);
  pinMode(ml2, OUTPUT);
  pinMode(mr1, OUTPUT);
  pinMode(mr2, OUTPUT);
  
}

void loop()
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, HIGH);
  
  digitalWrite(mr1, HIGH);
  digitalWrite(mr2, LOW);
  
  // for stopping motor
  //digitalWrite(ml1, LOW);
  //digitalWrite(ml2, LOW);
  
  //digitalWrite(mr1, LOW);
  //digitalWrite(mr2, LOW);
}
