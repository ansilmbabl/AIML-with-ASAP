//Write a C++ program to calculate area of square using function.

#include <iostream>
using namespace std;

void area();
int main()
{
    area();
    return 0;
}


void area()
{
    int l;
    cout<<"lenght of a side: ";
    cin>>l;
    int area = l * l;
    cout<< "area is: "<<area;
}
