//functions using parameter


#include <iostream>
using namespace std;

void number(int x)
{
    cout<< "enter a number: ";
    cin>>x;
    cout<<"your number is " << x;
}
int main()
{
    number(45);
    return 0;
}
