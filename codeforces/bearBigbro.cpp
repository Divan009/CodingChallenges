#include <iostream>
using namespace std;

int main(){
	int a, b;
	int year = 0;
	cin >> a >> b;
		
	while(a <= b){
		a = 3*a;
		b = 2*b;

		year++;
	}
	
	cout << year;
	return 0;
}