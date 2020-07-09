#define ll long long int
#include <bits/stdc++.h>

using namespace std;
int main(){
	int t;
	cin >> t;
	while(t--){
		ll a, b, c, d, ans, totalAlarmCycle;
		cin >> a >> b >> c >> d;
//if he has slept the least time req, a, and alarm
// rings after b time then op=b
		if(a <= b){
			cout << b <<"\n";
		}
		else if((c - d) < 0){
			cout << -1 <<"\n";
		}
		else{
			ans = b;
			ll more = a - b;
			ll one = c - d;
			totalAlarmCycle = ((more + one - 1)/one);
			ans = totalAlarmCycle*c+b;
			cout << ans <<"\n";
		}
	}
	return 0;
}