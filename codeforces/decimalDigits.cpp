 // There are N lines, each line always start with character 
 // ’0’ followed by ’.’, then unknown number of digits x, 
 // ﬁnally each line always terminated with three dots ”...”.

// input
// 2
// 0.1277...
// 0.1568979...

#include <iostream>
using namespace std;
char digits[100]; //use global var, good strategy in contests

int main(){
	int N;
	scanf("%d", &N);
	while(N--){
		scanf("0.%[0-9]...", &digits);
		printf("the digits are 0.%s\n", digits);
	}
}