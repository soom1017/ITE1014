#include <stdio.h>
int main()
{
	int arr[5];
	scanf("%d %d %d %d %d", arr, &*(arr+1), &*(arr+2), &*(arr+3), &*(arr+4));
	int* fptr = arr;
	int* bptr = arr+4;
	int i, temp;

	for(i=0;i<2;i++)
	{
		temp = *fptr;
		*fptr = *bptr;
		*bptr = temp;
		fptr += 1;
		bptr -= 1;
	}

	printf("%d %d %d %d %d\n", *arr, *(arr+1), *(arr+2), *(arr+3), *(arr+4));

	return 0;
}

