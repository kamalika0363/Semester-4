#include <stdio.h>
#include <graphics.h>
void bresenham(int x1, int y1, int x2, int y2)
{
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);
    int sx = x1 < x2 ? 1 : -1;
    int sy = y1 < y2 ? 1 : -1;
    int err = dx - dy;
    int x = x1, y = y1;
    putpixel(x, y, WHITE);
    while (x != x2 || y != y2)
    {
        int e2 = 2 * err;
        if (e2 > -dy)
        {
            err -= dy;
            x += sx;
        }
        if (e2 < dx)
        {
            err += dx;
            y += sy;
        }
        putpixel(x, y, WHITE);
    }
}

main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    int x1 = 100, y1 = 100, x2 = 300, y2 = 200;
    bresenham(x1, y1, x2, y2);
    getch();
    closegraph();
    return 0;
}
