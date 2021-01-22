#include <stdio.h>
void swap(char** pstr1, char** pstr2)
{
	char* temp = *pstr1;
	*pstr1 = *pstr2;
	*pstr2 = temp;
}
void printArray(char** arr, int len)
{
	printf("Array ");
	for(int i=0;i<len;i++)
		printf("[%d]:%s, ", i, arr[i]);
	printf("\n");
}
int main()
{
	char* strArr[2] = {"aaa", "bbb"};
	printArray(strArr, sizeof(strArr)/sizeof(char*));

	swap(&strArr[0], &strArr[1]);
	printArray(strArr, sizeof(strArr)/sizeof(char*));

	return 0;
}
		
