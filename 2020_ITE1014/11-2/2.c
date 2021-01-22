#include <stdio.h>
typedef struct
{
	char name[7];
	int score;
} Person;
void printScoreStars(Person* persons, int len)
{
	for(int i=0;i<len;i++)
	{
		printf("%-7s", persons[i].name);
		for(int k=0;k<(persons[i].score/5);k++)
			printf("*");
		printf("\n");
	}
}
int main()
{
	Person arr[3];
	for(int i=0;i<3;i++)
		scanf("%s %d", arr[i].name, &arr[i].score);
	printScoreStars(arr, 3);
	return 0;
}	
