#include<stdio.h> #include<conio.h> #include<graphics.h>
void boundaryFill(int x,int y,int b_c,int f_c)
{
int current = getpixel(x,y);
if ((current!=b_c) && (current!=f_c))
{
putpixel(x,y,f_c); boundaryFill(x+1,y,15,f_c); boundaryFill(x-1,y,15,f_c); boundaryFill(x,y+1,15,f_c); boundaryFill(x,y-1,15,f_c);
}
}
void floodFill(int x, int y, int a_c, int f_c)
{
int current = getpixel(x,y);
if ((current==a_c) && (current!=f_c))
{
putpixel(x,y,f_c); floodFill(x,y+1,a_c,f_c); floodFill(x+1,y,a_c,f_c); floodFill(x,y-1,a_c,f_c); floodFill(x-1,y,a_c,f_c);
}}
int main()
{
int gd = DETECT,gm; int f_c,ff_c,x,y;
initgraph(&gd, &gm, "C:\TURBOC3\BIN"); clrscr();
printf("Enter Co-ordinates of seed pixel (x,y) :-\n"); scanf("%d %d",&x,&y);
printf("Enter fill colour value in integer :- "); scanf("%d",&f_c);
circle(320,240,25); boundaryFill(x,y,15,f_c); printf("Enter Flood Fill color:- "); scanf("%d",&ff_c); floodFill(x,y,f_c,ff_c);
getch();
closegraph();
return 0;
}
