#include <iostream>

using namespace std;

int main(){
	int n=0;
	cin >> n;
	int stillNow = 0, capacity = 0;
	while(n--){
		int a, b;
		cin >> a >> b;
		stillNow -= a;
		stillNow += b; 
		capacity = max(capacity, stillNow);
	}
	cout << capacity;
	return 0;
}