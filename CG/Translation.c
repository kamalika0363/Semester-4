#include <stdio.h> 
#include<graphics.h> 
int main(){ 
int x1,y1,x2,y2,tx,ty; 
int gd = DETECT,gm; 
initgraph(&gd, &gm, "C://TURBOC3/BGI"); printf("Enter the X Co-Ordinate: "); 
scanf("%d %d",&x1, &x2); 
printf("Enter the Y Co-Ordinates: "); 
scanf("%d %d",&y1, &y2); 
printf("Enter the translation factor in x direction: "); 
scanf("%d",&tx); 
printf("Enter the translation factor in y direction: "); 
scanf("%d",&ty); 
line (x1,y1,x2,y2); 
x1 += tx; 
y1 += ty; 
x2 += tx; 
y2 += ty; 
setcolor(RED); 
line(x1,y1,x2,y2); 
getch(); 
closegraph(); 
return 0; 
} 
