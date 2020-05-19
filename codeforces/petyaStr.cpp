#include <bits/stdc++.h>

using namespace std;

int main(){
	string str, str1;

	cin >> str >> str1;
	
	transform(str.begin(), str.end(), str.begin(), ::tolower);
	transform(str1.begin(), str1.end(), str1.begin(), ::towlower);

	if (str == str1){
		cout << 0<< "\n";
	}
	else if (str > str1)
		cout << 1 << "\n";
	else 
		cout << -1 << "\n";
}