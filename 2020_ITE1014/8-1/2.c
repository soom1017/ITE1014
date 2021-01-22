#include <stdio.h>
int addTotal(int a)
{
	int added = 0;
	for(int i=1;i<=a;i++)
		added = added + i;
	return added;
}

int gMul=1;

int mulTotal(int a)
{
	for(int i=1;i<=a;i++)
		gMul = gMul*i;
}

int main()
{
	int n;
	scanf("%d", &n);
	printf("addTotal(): %d\n", addTotal(n));
	mulTotal(n);
	printf("gMul: %d\n", gMul);
	return 0;
}
