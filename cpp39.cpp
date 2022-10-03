#include<stdio.h>
main()
{
	int a,b;
	printf("Enter first number:");
	scanf("%d",&a);
	printf("Enter second number:");
	scanf("%d",&b);
	a,b=b,a;
	printf("The original numbers are %d %d\n",a,b);
	printf("The swapped numbers are %d %d\n",b,a);
}
