#include <iostream>
using namespace std;

class det
{
public:
    det(string name, int number) //constructor
    {
        cout<<name<<"welcome here........."<<" your number is "<<number;
    }
};

int main()
{
    det stud("ansil ",1212);
    return 0;
}
