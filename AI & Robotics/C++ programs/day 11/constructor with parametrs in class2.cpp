#include <iostream>
using namespace std;

class det{
public:
string group (string num);
};

string det::group(string num)
{
return num;
}

int main()
{
det abcd;
    cout<<abcd.group("abcd");
    return 0;
}

