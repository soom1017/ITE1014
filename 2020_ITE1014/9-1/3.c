#include <stdio.h>
int main()
{
	char str[40];
	scanf("%s", str);
	int length = 0;
	for(int i=0;i<sizeof(str)/sizeof(char);i++)
	{
		if(str[i] == '\0')
			break;
		else
			length += 1;
	}
	printf("%d\n", length);	
	return 0;
}
