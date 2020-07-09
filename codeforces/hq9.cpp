// ip- "shvbchdbvhbhvH2847ry290*&(*@&#)(@#)-"sdhcbsh"
#include <bits/stdc++.h>
using namespace std;

int main(){
	string s;
	cin >> s;
// do not use s[i] to traverse
// bcz if input has a single quote
// then it will stop traversing in the middle

	for(int i=0; i < s.length(); ++i){
		if(s[i]=='H' || s[i]=='Q' || s[i]=='9'){
			cout << "YES";
			return 0;	
		}	
	}
	
	cout << "NO";
	return 0;
}