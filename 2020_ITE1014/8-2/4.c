#include <stdio.h>
int comb(int n, int r)
{
	if(r == 0)
		return 1;
	else if(r == 1)
		return n;
	else if(n == r)
		return 1;
	else
		return comb(n-1,r-1) + comb(n-1,r);
}
int main()
{
	int n;
	int r;
	scanf("%d %d", &n, &r);
	printf("%d\n", comb(n, r));
}
