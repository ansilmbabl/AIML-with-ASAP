#include <iostream>
using namespace std;

void number(string name);
string end();
int main()
{
    number("ansil");
    cout<< end();
    return 0;
}

string end()
{
    return "\nthank you";
}

void number(string name)
{
    cout<<"your name is " << name;
}
