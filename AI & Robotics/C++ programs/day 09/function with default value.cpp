#include <iostream>
using namespace std;

void name (string name = "name")
{
    cout<<"hiii "<< name<<endl;
}

int main()
{
    name("ansil");
    name("XYZ");
    name();
    name("ABCD");
    return 0;
}

