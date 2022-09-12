#include <stdio.h>

#define MAX_SIZE 1000
void combSort(int a[], int n);

int main()
{
    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i)
    {
        int num;
        int a[MAX_SIZE];
        scanf("%d", &num);
        for (int j = 0; j < num; j++)
            scanf("%d", &a[j]);
        combSort(a, num);
    }
    return 0;
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

/* comb sort 함수 */
void combSort(int a[], int n)
{
    int countCmpOps = 0; //비교 연산자 실행 횟수
    int countSwaps = 0;  // swap 함수 실행 횟수

    int gap = n;
    int shrink = 1.3;

    bool sorted = false;

    while (sorted == false)
    {
        gap = gap / shrink;
        if (gap <= 1)
        {
            gap = 1;
            sorted = true;
        }
        else if (int i = 0)
        {
        }
    }
    printf("%d %d ", countCmpOps, countSwaps);
}