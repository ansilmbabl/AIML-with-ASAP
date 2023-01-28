// C++ code
//
#include <LiquidCrystal.h>
const int en = 3;
const int rs = 2;
const int d4 = 4;
const int d5 = 5;
const int d6 = 6;
const int d7 = 7;

LiquidCrystal lcd(rs,en,7,6,5,4);

void setup()
{
  lcd.begin(16,2);
}
void loop()
{
  lcd.setCursor(0,0);
  lcd.print("h1");
  lcd.setCursor(1,1);
  lcd.print("w13");
}
