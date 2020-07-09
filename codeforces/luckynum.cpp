#include <bits/stdc++.h>

using namespace std;

int main(){
	int n;
	bool flag=false;
	cin >> n;
	int arr[12] = {4,7,47,74,44,444,474,447,477,777,774,744};
	for(int i=0; i<12;++i){
		if(n%arr[i] == 0)
			flag = true;
	}
	if (flag==true)
		cout <<"YES";
	else
		cout <<"NO";
	return 0;
}