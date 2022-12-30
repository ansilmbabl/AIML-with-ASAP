#include <iostream>
using namespace std;

void number();
int main()
{
    number();
    return 0;
}

void number()
{
    int x;
    cout<<"enter a number: ";
    cin>>x;
    cout<<"your number is " << x;
}
