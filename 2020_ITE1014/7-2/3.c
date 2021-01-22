#include <stdio.h>
int main()
{
	char a;
	while(1)
	{
		scanf(" %c", &a);
		if(a >= 65 && a <= 90)
			printf("-> %c\n", a+32);
		else if(a >= 97 && a <= 122)
			printf("-> %c\n", a-32);
		else if(a >= 47 && a <= 57)
			printf("%c\n", a);
		else
		{
			printf("exit\n");
			break;
		}
	}
	return 0;
}
