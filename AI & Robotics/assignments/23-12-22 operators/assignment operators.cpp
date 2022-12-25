#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int x=5,y;
    cout << "number is : "<<x;
    cout << "\nenter number to be operated : ";
    cin>>y;

    //assignment operators
    cout <<"(x+=y) = "<<(x+=y);
    cout <<"\n(x-=y) = "<<(x-=y);
    cout <<"\n(x*=y) = "<<(x*=y);
    cout <<"\n(x/=y) = "<<(x/=y);
    cout <<"\n(x%=y) = "<<(x%=y);

    return 0;
}
