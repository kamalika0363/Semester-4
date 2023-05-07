#include <stdio.h>
#include <graphics.h>

void DDA(int x1, int y1, int x2, int y2)
{
    int dx = x2 - x1;
    int dy = y2 - y1;
    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);
    float xIncrement = dx / (float) steps;
    float yIncrement = dy / (float) steps;
    float x = x1, y = y1;
 
    putpixel(x, y, WHITE);
 
    for (int i = 0; i < steps; i++)
    {
        x += xIncrement;
        y += yIncrement;
        putpixel(x, y, WHITE);
    }
}

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\TURBOC3\BGI");
 
    int x1 = 100, y1 = 100, x2 = 300, y2 = 200;
    DDA(x1, y1, x2, y2);
 
    getch();
    closegraph();
    return 0;
}
