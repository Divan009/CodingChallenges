#include <iostream>
using namespace std;

int main(){
	string keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./";

	char l[2];
	cin >> l;

	string input;
	cin>>input;
	
	if (l[0] == 'R'){
		for(int i = 0; i<input.length(); i++){
			for(int j=0; j<keyboard.length(); ++j){
				if(input[i] == keyboard[j]){
					cout << keyboard[j-1];
					break;
				}
			}
		}
		cout<<"\n";
	}else{
		for(int i = 0; i<input.length(); i++){
			for(int j=0; j<keyboard.length(); ++j){
				if(input[i] == keyboard[j]){
					cout << keyboard[j+1];
					break;
				}
			}
		}
		cout << "\n";
	}
	return 0;
}


