// C++ code
// motor rotation with functions

int ml1 = 5; // input1
int ml2 = 2; // input2
int mr1 = 8; // input3
int mr2 = 10; // input4

void setup()
{
  pinMode(ml1, OUTPUT);
  pinMode(ml2, OUTPUT);
  pinMode(mr1, OUTPUT);
  pinMode(mr2, OUTPUT);
  
}

void loop() //main function
{
  forward();
    delay(1000);
    
  stop();
    delay(1000);
    
  backward();
    delay(1000);
}

void forward() // forward function
{
  digitalWrite(ml1, HIGH);
  digitalWrite(ml2, LOW);
  digitalWrite(mr1, HIGH);
  digitalWrite(mr2, LOW);
}
  
void stop() // stop function
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, LOW);
  digitalWrite(mr1, LOW);
  digitalWrite(mr2, LOW);
}
  
void backward() // backward function
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, HIGH);
  digitalWrite(mr1, LOW);
  digitalWrite(mr2, HIGH);
}
