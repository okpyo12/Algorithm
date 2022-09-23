#include <stdio.h>

int factorial(int a);
int main()
{
    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i)
    {
        int num;
        scanf("%d", &num);
        int answer = factorial(num) % 1000;
        printf("%d \n", answer);
    }
}

int factorial(int a)
{
    if (a <= 1)
    {
        return 1;
    }
    else
    {
        int num = factorial(a - 1) * a;
        while (num % 10 == 0)
        {
            num /= 10;
        }
        return num % 10000;
    }
}