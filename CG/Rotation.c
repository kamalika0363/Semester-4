#include <graphics.h>
#include <math.h>
#include <stdio.h>
#include <conio.h>
main() {
 int x1,y1,x2,y2;
 float angle,radians,s,c;
 int x1_new,y1_new,x2_new,y2_new;
 int gd = DETECT, gm;
 initgraph(&gd, &gm, "");
 printf("Enter coordinates of line\n");
 scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
 line(x1, y1, x2, y2);
 putpixel(x1,y1,GREEN);
 putpixel(x2,y2,RED);
 printf("Enter a rotating angle\n");
 scanf("%f",&angle);
 radians = angle * M_PI / 180;
 s = sin(radians);
 c = cos(radians);
 x1_new =floor(x1 * c + y1 * s);
 y1_new =floor(-x1 * s + y1 * c);
 x2_new =floor(x2 * c + y2 * s);
 y2_new =floor(-x2 *s + y2 * c);
 line(x1_new, y1_new, x2_new, y2_new);
 putpixel(x1_new,y1_new,GREEN);
 putpixel(x2_new,y2_new,RED);
 getch();
 closegraph();
}
