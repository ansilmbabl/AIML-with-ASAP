#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int x=5,y;
    cout << "number is : "<<x;
    cout << "\nenter number to be compared : ";
    cin>>y;
    cout<<"0 = False\n1 = True\n\n";

    cout<<"x==y gives "<<(x==y);
    cout<<"\nx!=y gives "<<(x!=y);
    cout<<"\nx>y gives "<<(x>y);
    cout<<"\nx<y gives "<<(x<y);
    cout<<"\nx>=y gives "<<(x>=y);
    cout<<"\nx<=y gives "<<(x<=y);

}
