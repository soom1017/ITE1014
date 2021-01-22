#include <stdio.h>
#include <string.h>
int palin(char str[]);
int main()
{
	char word[10];
	scanf("%s", word);

	if(palin(word) == 1)
		printf("This is a palindrome\n");
	else printf("This is not a palindrome\n");

	return 0;
}
int palin(char str[])
{
	int leng = strlen(str);
	int i;
	for(i=0;i<(leng/2);i++)
        {
                if(str[i] != str[leng-1-i])
                        break;
                if(i == leng/2 -1)
                        return 1;
        }

	return 0;
}
