#include <iostream>
#include <algorithm>
 
using namespace std;
 
int main(){
	int k, a[12], total=0,sum=0, counter=0;
	cin >> k;
	for(size_t i=0; i<12; ++i){
		cin >> a[i];
		total+=a[i];
	}
 
	int n = 12; //sizeof(a)/sizeof(a[0])
 
	if(k==0){
		cout << 0; 
		return 0;
	}

	if(total < k){
		cout << -1;
	}else{
		sort(a, a+n);
		for(int i=n-1; i >= 0; --i){
			counter++;
			sum+=a[i];
			if(sum >= k){
				cout << counter;
				break;
			}
		}
	}
	
	return 0;
}