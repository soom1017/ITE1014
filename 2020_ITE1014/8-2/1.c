#include <stdio.h>
void printLine(int n)
{
	for(int i=1;i<=n;i++)
		printf("%d ", i);
	printf("\n");
}
int main()
{
	int n;
	scanf("%d", &n);	
	for(int i=1;i<=n;i++)
		printLine(i);
	for(int i=n;i>=1;i--)
		printLine(i);
	return 0;
}
