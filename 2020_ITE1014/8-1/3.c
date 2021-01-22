#include <stdio.h>
int recursive(int n)
{
	if(n == 0)
		return 0;
	else
		return n + recursive(n-1);
}
int main()
{
	int n;
	scanf("%d", &n);
	printf("%d\n", recursive(n));
	return 0;
}
