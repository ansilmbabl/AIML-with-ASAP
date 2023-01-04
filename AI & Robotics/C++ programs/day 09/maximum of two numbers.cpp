//Write a program that ask for two numbers, compare them and show the maximun.Declare a function called max_twothat compares the numbers and returns the maximun.

#include <iostream>
using namespace std;

int max_two(int x,int y)
{
    if (x==y)
    {
        cout << "same numbers";
    }
    else if (x>y)
    {
        cout << x;
    }
    else
    {
        cout << y;
    }
}

int main()
{
    int x,y;
    cout<<"first number: ";
    cin>>x;
    cout<<"second number: ";
    cin>>y;
    max_two(x,y);
    return 0;
}
