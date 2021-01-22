#include <stdio.h>
typedef struct person {
	char name[10];
	int age;
} Person;
int main()
{
	Person p1;
	scanf("%s %d", p1.name, &p1.age);
	printf("name: %s\n", p1.name);
	printf("age: %d\n", p1.age);

	return 0;
}
