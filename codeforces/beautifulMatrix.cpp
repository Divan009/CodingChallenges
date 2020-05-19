#include <bits/stdc++.h>

using namespace std;

int main(){
	int x, ans = 0;

	for (int r = 1; r <= 5; ++r){
		for(int c = 1; c <= 5; ++c){
			cin >> x;
			if (x == 1){
				ans = abs(r-3)+abs(c-3);
			}
		}
	}
	cout << ans <<"\n";
	return 0;
}