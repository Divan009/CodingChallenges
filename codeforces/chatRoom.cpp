#include<bits/stdc++.h>
using namespace std;

// int main(){
	// string s, word = "hello";
	// cin >> s;

	// int a, counter = 0;

	// for(int i = 0; i < s.size()-1; ++i){
	// 	if(s[i]== word[a]){
	// 		a++;
	// 		counter++;

	// 		if (counter==5)
	// 			break;
	// 	}
	// }
	// if (counter==5){
	// 	cout << "YES";
	// }
	// else
	// 	cout << "NO";

	string a, b = "hello";
	int j = 0, pas = 0;
	int main() {
	    cin >> a;
	    for (int i = 0; i < a.size(); i++) {
	        if (a[i] == b[j]) {
	            j++;
	            pas++;
	            
	            if (pas == 5) {
	                break;
	            }
	        }
	    }
	    if (pas == 5) {
	        cout << "YES";
	    } else {
	        cout << "NO";
	    }
	return 0;
}