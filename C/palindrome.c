#include <stdio.h>

int main(void)
{
int a,b,n,sum=0;
scanf("%d",&a);
n=a;
while(a>0)
{
b=n%10;
sum=sum*10+b;
n=n/10;
}
if(a==sum)
printf("yes");
else
printf("no");
return 0;
}
