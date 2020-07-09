// THIS CODE IS A PIECE OF SHIT
// UPTO SERIOUS REVIEW
// input:
// 50
// 2 2 3 4 5 4 4 5 7 3 2 7 = 48
// and u will see, IM NOT JK

// WHAT THE LEGIT FUCKKKKKKKKKKK
// NEVERRRRR DO for(int i=0; i<a[12]; ++i)
// the problem is a[12]

#include <iostream>
#include <algorithm>
// #include <numeric>

using namespace std;

int main(){
	int k=0, bsum=0, sum2=0, counter=0; 
	cin >> k;
	

	// if(k==0){
	// 	cout << 0; 
	// 	return 0;
	// }
	

	// when u want to read in an array dont use a[12] in array
	int a[12]; 
	for(int i=0; i<12; ++i)
		cin >> a[i];

	// for(int i=0; i<a[12]; ++i)
	// 	cout << a[i];
	

	int n = 12;//sizeof(a)/sizeof(a[0]);


	// bsum = accumulate(a, a+n, bsum);
	// if(k > bsum){
	// 	cout << "hello people";
	// 	return 0;
	// }

	// sort(a, a+n);

	// for(int i=n-1; i > 0; --i){
	// 	counter++;
	// 	sum2+=a[i];
	// 	if(sum2 >= k){
	// 		cout << counter;
	// 		break;
	// 	}
	// }

	return 0;
}