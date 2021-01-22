#include <stdio.h>
typedef struct
{
	int xpos;
	int ypos;
} Point;
Point getScale2xPoint(const Point* pp)
{
	Point p_new;
	p_new.xpos = pp->xpos*2;
	p_new.ypos = pp->ypos*2;
	return p_new;
}
int main()
{
	Point p1;
	scanf("%d %d", &p1.xpos, &p1.ypos);
	Point p2 = getScale2xPoint(&p1);
	printf("%d %d\n", p2.xpos, p2.ypos);

	return 0;
}
