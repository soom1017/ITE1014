#include <stdio.h>
int add(int a, int b)
{
	int added = a + b;
	return added;
}
int sub(int a, int b)
{
	int subed = a - b;
	return subed;
}
int mul(int a, int b)
{
	int muled = a*b;
	return muled;
}
double div(double a, double b)
{
	double dived = a/b;
	return dived;
}
int mod(int a, int b)
{
	int moded = a%b;
	return moded;
}
void printMsg()
{
	printf("completed\n");
}

int main()
{
	int first;
	int second;
	scanf("%d\n%d", &first, &second);
	printf("sum: %d\n", add(first, second));
	printf("difference: %d\n", sub(first, second));
	printf("product: %d\n", mul(first, second));
	printf("division: %f\n", div(first, second));
	printf("remainder: %d\n", mod(first, second));
	printMsg(first, second);

	return 0;
}
