#include <stdio.h>
#include <string.h>

int main()
{
	char word1[20];
	char word2[20];

	scanf("%s %s", word1, word2);
	printf("str1: %s\n", word1);
	printf("str2: %s\n", word2);
	
	printf("length of str1: %ld\n", strlen(word1));
	printf("length of str2: %ld\n", strlen(word2));
	
	printf("str1+str2: %s%s\n", word1, word2);
	
	if(strcmp(word1, word2) == 0)
		printf("same\n");
	else printf("not same\n");
	
	return 0;
}
