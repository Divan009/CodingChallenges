#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int col; 
	cin >> col;

	if (col==0){
		cout << 0;
		return 0;
	}

	int arr[col];

	for(int i=0; i < col; ++i){
		cin >> arr[i];
	}
	

	sort(arr, arr+col);

	for(int i=0; i < col; ++i)
		cout << arr[i] << " ";

	return 0;
}