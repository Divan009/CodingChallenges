#include <bits/stdc++.h>

using namespace std;

int main(){
	string inp, op;
	cin >> inp;
	int len = inp.length();
	for(int i=0;i<len; i++){
		if (inp[i]=='a' || inp[i]=='e' ||
			inp[i]=='i' || inp[i]=='o' ||
			inp[i]=='u' || inp[i]=='y' ||
			inp[i]=='A' || inp[i]=='E' ||
			inp[i]=='I' || inp[i]=='O' ||
			inp[i]=='U' || inp[i]=='Y')
			continue;
		else{
			op+='.';
			op+=towlower(inp[i]);
		}
	}
	cout << op;
}