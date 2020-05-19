//5
//RRRRR
//op-4
#include <bits/stdc++.h>
//this is at a big fault
using namespace std;

int main(){
	int n, counter = 1;
	string s;
	cin >> n >> s;
	for(int i=0; i < n; ++i)
		if(s[i] == s[i+1])
			counter += 1;
	cout << counter-1;
	
	return 0;
}