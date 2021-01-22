#include <stdio.h>
void square(double* pvar)
{
	*pvar = (*pvar)*(*pvar);
}

int main()
{
	double dvar;
	scanf("%lf", &dvar);
	square(&dvar);
	printf("%f\n", dvar);

	return 0;
}
