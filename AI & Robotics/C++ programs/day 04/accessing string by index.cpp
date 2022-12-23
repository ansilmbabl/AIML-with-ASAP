#include <iostream>
#include <string>
using namespace std;


int main(){
string s = "welcome dear friend";
cout << s[0]; //return "w"

string a = s.substr(0,7);
cout << "\n" << a;
return 0;
}
