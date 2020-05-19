//1100000000001
#include <bits/stdc++.h>

using namespace std;

int main(){
	string n;
	int counter = 1;
	cin >> n;
	for(unsigned i = 0; i < n.length()-1; ++i){
		if(n[i] == n[i+1]){
			counter += 1;
			if(counter >= 7){
				cout << "YES" <<"\n";
				return 0;
			}			
		}
		else{
			counter = 1;
		}
	}
	cout << "NO";
	return 0;
}