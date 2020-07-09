//inputs
// 3
//2 1 2
//output = 2 coins



#include <bits/stdc++.h>
using namespace std;

int main(){
	int n, counter=0;
	cin >> n;
	int arr[n];
	int sum = 0, sum2 = 0;
	for(int i=0; i<n; ++i){
		cin>>arr[i];
		sum+=arr[i];
	}
	sort(arr,arr+n);
	int halfCoinVal = sum/2; // 5/2=2
	// traversing from 1 2 2<-- to get max val w minimum coins
	for(int i=n-1; i>=0; --i){
		counter++;
		sum2 += arr[i];
		if(sum2 > halfCoinVal){
			cout << counter;
			break;
		}
	}
	return 0;
}


