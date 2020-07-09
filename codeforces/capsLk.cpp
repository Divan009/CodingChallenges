//errrorrrrrr
#include <bits/stdc++.h>
using namespace std;

int main(){
	string s;
	cin >> s;
//if first char is between a and z, then cap it
	if(s[0]>=97 && s[0]<=122){
		s[0]=s[0]-32;
	}
	for(int i=1; i<s.length(); ++i){
		if(s[i]>=65 && s[i]<=90){
			s[i]=s[i]+32;
		}
	}
	cout <<s;
	return 0;
}
//rules
// 1 if first letter is lowercase, and the others are not, 
// 	then it needs to be changed
// 2 if all of them are in caps

// exaample:
// cAPLoCK - requires no changing
// cAPLOCK - changed it to Caplock
// AND - needs to be changed to And