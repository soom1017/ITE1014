#include <stdio.h>
#include <string.h>

int main()
{
	char word[10];
	scanf("%s", word);

	for(int i=0;i<strlen(word);i++)
	{
		if(65<=word[i] && word[i]<=90)
			word[i] = word[i] + 32;
		else word[i] = word[i] - 32;
	}
	
	printf("%s\n", word);
	return 0;
} 
