#include <graphics.h>
#include <stdio.h>


void flood(int x, int y, int new_col, int old_col)
{
	
	if (getpixel(x, y) == old_col) {

		
		putpixel(x, y, new_col);

		
		flood(x + 1, y, new_col, old_col);

		
		flood(x - 1, y, new_col, old_col);

		
		flood(x, y + 1, new_col, old_col);

		
		flood(x, y - 1, new_col, old_col);
	}
}

int main()
{
	int gd, gm = DETECT;

	// initialize graph
	initgraph(&gd, &gm, "");

	// rectangle coordinate
	int top, left, bottom, right;

	top = left = 50;
	bottom = right = 300;

	// rectangle for print rectangle
	rectangle(left, top, right, bottom);

	// filling start coordinate
	int x = 51;
	int y = 51;

	// new color to fill
	int newcolor = 12;

	// new color which you want to fill
	int oldcolor = 0;

	// call for fill rectangle
	flood(x, y, newcolor, oldcolor);
	getch();

	return 0;
}
