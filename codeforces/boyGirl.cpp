#include <bits/stdc++.h>

using namespace std;

int main(){
	string str;
	int counter = 0;
	cin >> str;
	sort(str.begin(), str.end());
	// for(int i=0; i < str.length()-1; ++i){
	// 	if(str[i]!=str[i+1]){
	// 		counter+=1;
	// 	}
	// }
	str.erase(unique(str.begin(), str.end()), str.end());
    if (str.length() % 2 == 0){
        cout << "CHAT WITH HER!" << endl;
    }
    else
    {
        cout << "IGNORE HIM!" << endl;
    }
	//if (counter%2==0){
	// 	cout << "IGNORE HIM!" <<"\n";
	// }else{		
	// 	cout << "CHAT WITH HER!";
	// }
	return 0;
}