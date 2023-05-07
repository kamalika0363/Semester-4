#include<graphics.h>
#include<math.h>
#include<conio.h>
#include<stdio.h>
void main()
{
int x1,x2,x3,x4,y1,y2,y3,y4;
double put_x,put_y,u;
int gd=DETECT,gm;
initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
printf("\n****** Bezier Curve ***********");
printf("\n Please enter x and y coordinates ");
scanf("%d %d %d %d %d %d %d %d",&x1,&y1,&x2,&y2,&x3,&y3,&x4,&y4);
setcolor(GREEN);
line(x1,y1,x2,y2);
line(x2,y2,x3,y3);
line(x3,y3,x4,y4);
line(x4,y4,x1,y1);
for(u=0.0;u<=1.0;u=u+0.001){
put_x = pow(1-u,3)x1 + 3*u*pow(1-u,2)*x2 + 3*u*u(1-u)*x3 + pow(u,3)*x4;
put_y = pow(1-u,3)y1 + 3*u*pow(1-u,2)*y2 + 3*u*u(1-u)*y3 + pow(u,3)*y4;
putpixel(put_x,put_y,7);
}
getch();
closegraph();
}
