#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
	int T;
	scanf("%d\n", &T);
	for(int t=0; t<T; t++)
	 {
		int n;
		scanf("%d\n", &n);
		int inp[10000];

		int min = 0x7fffffff;
		for (int i=0; i<n; i++) {
			scanf("%d", &inp[i]);
			if (inp[i] < min) 
				min = inp[i];
		}

// In this problem I used reverse approach, in which we decrease the element upto it get equal to minimum element.
		int min_count = 0x7fffffff;
		for( int j=-5; j <= 0; j++) {
			int count= 0;
			for(int i=0; i<n; i++) {
				int diff = inp[i] - (min+j);
				count += diff / 5;
				diff = diff % 5;
				count += diff / 2;
				diff = diff % 2;
				count += diff;
			}
			if (count < min_count)
				 min_count = count;
		}
		printf("%d\n", min_count);
	}	
    return 0;
}