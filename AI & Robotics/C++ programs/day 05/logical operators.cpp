#include <iostream>
using namespace std;

int main(){
int x=5;
cout<< "1=true\t0=false\n\n";
cout<< "(x<6 && x>2) : "<<(x<6 && x>2) <<"\n";
cout<< "(x>6 || x>2) : "<<(x>6 || x>2) <<"\n";
cout<< "!(x<6 && x>2) : "<<!(x<6 && x>2);

return 0;

}
