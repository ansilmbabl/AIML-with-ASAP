#include <iostream>
using namespace std;

int main(){
int i;
while (i<10){
if (i == 4){
i++;
continue;
}
if (i == 8){
break;}
cout<<i<<"\n";
i++;
}
return 0;
}
