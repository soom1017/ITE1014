#include <stdio.h>
int main()
{
	int i; double d; char c;
	scanf("%d %lf %c", &i, &d, &c);

	printf("i: %d, %p\n", i, &i);
	printf("d: %f, %p\n", d, &d);
	printf("c: %c, %p\n\n", c, &c);

	int* pi = &i; double* pd = &d; char* pc = &c;
	(*pi) += 1; (*pd) += 1; (*pc) += 1;
	
	printf("i+1: %d\n", i);
	printf("d+1: %f\n", d);
	printf("c+1: %c\n\n", c);

        printf("size of pi: %ld\n", sizeof(pi));
        printf("size of pd: %ld\n", sizeof(pd));
        printf("size of pc: %ld\n", sizeof(pc));

	return 0;
}
