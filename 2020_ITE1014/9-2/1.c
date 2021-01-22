#include <stdio.h>
int main()
{
	int arr[5];
	scanf("%d %d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3], &arr[4]);
	int min = arr[0], max = arr[0];

	for(int i=0;i<5;i++)
	{
		if(arr[i] < min)
			min = arr[i];
	}

	for(int j=0;j<5;j++)
        {
                if(arr[j] > max)
                        max = arr[j];
        }

	int sum = 0;
	for(int k=0;k<5;k++)
		sum = sum + arr[k];

	printf("min: %d\n", min);
	printf("max: %d\n", max);
	printf("sum: %d\n", sum);

	return 0;
}
