#include <stdio.h> 
#include<graphics.h> 
#include <math.h> 
int main(){ 
int gd = DETECT,gm; 
initgraph(&gd, &gm, "C://TURBOC3/BGI"); 
int x1,x2,y1,y2,theta; 
printf("Enter the X Co-ordinate: "); scanf("%d , %d", &x1, &x2); 
printf("Enter the Y Co-ordinate: "); scanf("%d , %d", &y1, &y2); 
printf("Enter Theta"); 
scanf("%d", &theta); 
theta = 45*M_PI/180; 
setcolor(RED); 
line(x1,y1,x2,y2); 
int x1_new, y1_new, x2_new, y2_new; x1_new = round(x1 * cos(theta) - y1*sin(theta)); y1_new = round(x1 * sin(theta) - y1*cos(theta)); x2_new = round(x2 * cos(theta) - y2*sin(theta)); y2_new = round(x2 * sin(theta) + y2*cos(theta)); setcolor(GREEN); 
line(x1_new,y1_new,x2_new,y2_new); getch(); 
closegraph(); 
return 0; 
}