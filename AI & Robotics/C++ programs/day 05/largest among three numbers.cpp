#include <iostream>
using namespace std;

int main(){
int x,y,z;
cout<< "enter num 1: ";
cin>>x;
cout<< "enter num 2: ";
cin>>y;
cout<< "enter num 3: ";
cin>>z;

if (x>y && x>z)
    {
        cout<<"largest number is : "<<x;
    }
else if (x<y && y>z)
    {
        cout<<"largest number is : "<<y;
    }
else
    {
        cout<<"largest number is : "<<z;
    }
return 0;
}
