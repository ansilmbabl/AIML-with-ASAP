// C++ code
// turning the robot

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
  right_turn();
}

void left_turn() // turning left
{
  digitalWrite(ml1, LOW);
  digitalWrite(ml2, HIGH);
  digitalWrite(mr1, HIGH);
  digitalWrite(mr2, LOW);
}
  
void right_turn() // turning right
{
  digitalWrite(ml1, HIGH);
  digitalWrite(ml2, LOW);
  digitalWrite(mr1, LOW);
  digitalWrite(mr2, HIGH);
}
