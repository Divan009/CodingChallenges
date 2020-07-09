#include <iostream>
using namespace std;

int main(){
	int k, n, w;
	long long cost=0;

	cin >> k >> n >> w;

	for(int i = 1; i <= w; ++i){
		cost += k*i;
	}
	if (n >= cost)
		cout << 0 <<"\n";
	else
		cout << cost - n << "\n";

	return 0;
}