#include <stdio.h>

int main(void)
{
int a,b,mul=1,i;
scanf("%d",&a);
scanf("%d",&b);
for(i=1;i<=b;i++)
 {
  mul=mul*a;	
 }
printf("%d",mul);
return 0;
}
