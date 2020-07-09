#include <iostream>

using namespace std;
int main(){
	long long n, k, res;
	cin >> n >> k;
	if(k <= (n+1)/2){
		cout << 2*k-1 <<"\n";
	}
	else{
		cout << 2*(k-(n+1)/2);
	}
	// while (cin >> n, k)
	// {
	// 	if (n&1) //if it is odd
	// 	{
	// 		res = n/2 + 1;//n=[o,o,o,o,e,e,e] res=7/2+1=4, k=7

	// 		if(k<=res)//[o,o,o,o] //k=3 then ans = 2*3-1=5
	// 			cout << 2*k-1 <<"\n";
	// 		else//[e,e,e]
	// 			cout << 2*(k-res) << "\n";//2*(7-4)=6
	// 	}
	// 	else
	// 	{
	// 		res = n/2;//[o,o,o,o,o,e,e,e,e,e] res = 10/2 = 5

	// 		if(k<=res)
	// 			cout << 2*k-1 << "\n";
	// 		else
	// 			cout << 2*(k-res) <<"\n";
	// 	}
	// }
	return 0;
}
