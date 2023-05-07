#include<graphics.h>
#include<conio.h>
#include<stdio.h>
#include<math.h>
main()
{
int rcode_begin[4]={0,0,0,0},rcode_end[4]={0,0,0,0},region_code[4];
int W_xmin,W_ymin,W_xmax,W_ymax,flag=0;
float slope;
int x1,y1,x2,y2,i, xc,yc;
int gd=DETECT,gm;
initgraph(&gd,&gm,"");
printf("\nCohen Sutherlsnd Line Clipping algorithm");
printf("\n===========================================");
printf("\nEnter XMin, XMax =");
scanf("%d %d",&W_xmin,&W_xmax);
printf("\nEnter YMin, YMax =");
scanf("%d %d",&W_ymin,&W_ymax);
printf("\nEnter intial point x1 and y1= ");
scanf("%d %d",&x1,&y1);
printf("\nEnter final point x2 and y2= ");
scanf("%d %d",&x2,&y2);
cleardevice();
rectangle(W_xmin,W_ymin,W_xmax,W_ymax);
line(x1,y1,x2,y2);
line(0,0,getmaxx(),0);
line(0,0,0,getmaxy());
line(getmaxx(),0,getmaxx(),getmaxy());
line(0,getmaxy(),getmaxx(),getmaxy());
if(y1>W_ymax)  {
rcode_begin[0]=1;     // Top
flag=1 ;
}
if(y1<W_ymin) {
rcode_begin[1]=1;           // Bottom
flag=1;
}
if(x1>W_xmax)  {
rcode_begin[2]=1;           // Right
flag=1;
}
if(x1<W_xmin)   {
rcode_begin[3]=1;           //Left
flag=1;
}

//end point of Line
if(y2>W_ymax){
rcode_end[0]=1;           // Top
flag=1;
}
if(y2<W_ymin) {
rcode_end[1]=1;           // Bottom
flag=1;
}
if(x2>W_xmax){
rcode_end[2]=1;           // Right
flag=1;
}
if(x2<W_xmin){
rcode_end[3]=1;           //Left
flag=1;
 }
if(flag==0)
{
printf("No need of clipping as it is already in window");
}
flag=1;
for(i=0;i<4;i++){
region_code[i]= rcode_begin[i] && rcode_end[i] ;
if(region_code[i]==1)
 flag=0;
}
if(flag==0)
{
printf("\n Line is completely outside the window");
}
else{
slope=(float)(y2-y1)/(x2-x1);
if(rcode_begin[2]==0 && rcode_begin[3]==1)   //left
{
y1=y1+(float) (W_xmin-x1)*slope;
x1=W_xmin;

}
if(rcode_begin[2]==1 && rcode_begin[3]==0)       // right
{
y1=y1+(float) (W_xmax-x1)*slope;
x1=W_xmax;

}
if(rcode_begin[0]==1 && rcode_begin[1]==0)      // top
{
x1=x1+(float) (W_ymax-y1)/slope;
y1=W_ymax;
}
if(rcode_begin[0]==0 && rcode_begin[1]==1)     // bottom
{
x1=x1+(float) (W_ymin-y1)/slope ;
y1=W_ymin;
}
// end points
if(rcode_end[2]==0 && rcode_end[3]==1)   //left
{
y2=y2+(float) (W_xmin-x2)*slope;
x2=W_xmin;
}
if(rcode_end[2]==1 && rcode_end[3]==0)       // right
{
y2=y2+(float) (W_xmax-x2)*slope;
x2=W_xmax;
}
if(rcode_end[0]==1 && rcode_end[1]==0)      // top
{
x2=x2+(float) (W_ymax-y2)/slope;
y2=W_ymax;
}
if(rcode_end[0]==0 && rcode_end[1]==1)     // bottom
{
x2=x2+(float) (W_ymin-y2)/slope;
y2=W_ymin;

}
}
rectangle(W_xmin,W_ymin,W_xmax,W_ymax);
line(0,0,getmaxx(),0);
line(0,0,0,getmaxy());
line(getmaxx(),0,getmaxx(),getmaxy());
line(0,getmaxy(),getmaxx(),getmaxy());
setcolor(RED);
line(x1,y1,x2,y2);
getch();
closegraph();
}
