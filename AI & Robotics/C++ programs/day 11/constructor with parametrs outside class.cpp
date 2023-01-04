#include <iostream>
using namespace std;

class det
{
public:
    string name;
    int number;
    det(string x, int y); //constructor
};

det::det(string x, int y)
    {
        name = x;
        number = y;
    }

int main()
{
    det stud("ansil ",1212);
    cout<<stud.name<<"welcome here........."<<" your number is "<<stud.number;
    return 0;
}
