#include<stdio.h>

int main(void)
{
	int grades[4] = {73,67,38,33};

	for(int x =0; x < 4; x++){
		if(grades[x] >= 38 && grades[x] % 5 > 2 )
            		grades[x] = grades[x] + 5 - grades[x] % 5;
	}
	for(int i=0; i< 4; i++)
		printf("%d\n", grades[i]);

	return 0;
}
