#include <stdio.h>
#include <string.h>
int alreadyIn(char word[], char (*str)[21], int len)
{
	for(int i=0;i<len;i++)
	{
		if(strcmp(word, str[i]) == 0)
			return 1;
	}
	return 0;
}
void printArr(char (*str)[21], int len)
{
	printf("%d words in the list:\n", len);
	for(int i=0;i<len;i++)
		printf("%s ", str[i]);
	printf("\n");
}
int inTheList(char search[], char (*str)[21], int len)
{
	for(int i=0;i<len;i++)
	{
		if(strcmp(search, str[i]) == 0)
			return 1;
	}
	return 0;
}
int main()
{
	char word[21];
	char words[10][21];
	char search[21];
	int num = 0;
	while(1)
	{
		printf("Enter a word (Enter 'end' to quit): ");
		scanf("%s", word);

		if(strcmp(word, "end") == 0)
			break;

		else if(alreadyIn(word, words, num) == 1)
			printf("This word already exits. Please enter another word.\n");
		else
		{
			strcpy(words[num], word);
			num = num + 1;
		}
	}

	printArr(words, num);
	
	while(1)
	{
		printf("Enter a word to search (Enter 'end' to quit): ");
		scanf("%s", search);

		if(strcmp(search, "end") == 0)
                        break;
		
		if(inTheList(search, words, num) == 1)
			printf("This word is in the list.\n");
		else printf("This word is NOT in the list.\n");
	}
	return 0;
}
