// kefaa and first steps
// 2 2 1 3 4 1
// test 12 or 13 will be the death of me 

#include <bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin >> n;
	int a[n], counter=1, maxIncr=0;

 	if(n==1){
      	cout << 1;
      	return 0;
    }

	for(int i = 0; i < n; ++i){
		cin >> a[i];
	}

	for(int i=0; i < n-1; ++i){
		if (a[i] <= a[i+1]){
			counter += 1;
			if(maxIncr<counter)
				maxIncr=counter;
		}else{
			counter=1;
		}
	}
	cout << maxIncr;
	return 0;
}