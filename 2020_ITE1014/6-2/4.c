#include <stdio.h>
int main()
{
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	if(a >= b)
	{
		if(a >= c)
		{
			if(b >= c)
			{
				printf("min: %d\n", c);
				printf("max: %d\n", a); //a >= b >= c
			}
			else
			{
				printf("min: %d\n", b); 
                                printf("max: %d\n", a); //a >= c > b
			}
		}
		else
		{
                                printf("min: %d\n", b); 
                                printf("max: %d\n", c); //c > a >= b
		}
	}
	else
	{
                if(b >= c)
                {

                        if(c >= a)
                        {
                                printf("min: %d\n", a); 
                                printf("max: %d\n", b); //b >= c >= a
                        }
                        else
                        { 
                                printf("min: %d\n", c); 
                                printf("max: %d\n", b); //b > a > c
                        }
		}
		else
		{
			printf("min: %d\n", a);
			printf("max: %d\n", c); //c > b > a
		}
	}
	return 0;
}
	
