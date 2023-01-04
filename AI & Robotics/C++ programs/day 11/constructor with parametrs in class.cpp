#include <iostream>
using namespace std;

class det{
public:
int group (int num);
};

int det::group(int num)
{
return num;
}

int main()
{
det abcd;
    cout<<abcd.group(50);
    return 0;
}

