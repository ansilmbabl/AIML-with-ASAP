//program to add two numbers using a function

#include <iostream>
using namespace std;

int add(int x,int y)
{
    return x+y;
}

int main()
{
    int x,y;
    cout<<"first number: ";
    cin>>x;
    cout<<"second number: ";
    cin>>y;
    cout<<add(x,y);
    return 0;
}
