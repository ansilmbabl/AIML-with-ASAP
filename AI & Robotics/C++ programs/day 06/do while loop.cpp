//do while loop
//find sum  of all numbers from 1 to 10

#include <iostream>
using namespace std;

int main()
{
    int i=1,sum =0;
    do
        {
            sum += i;
            i++;
        }
    while (i<=10);
    cout<<sum;
    return 0;
}
