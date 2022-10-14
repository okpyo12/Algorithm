#include <iostream>

using namespace std;

#define MAX_SIZE 100

int Kadane(int v[], int n, int *start, int *end);
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        int num, value, a[MAX_SIZE];
        int start = -1;
        int end = -1;
        cin >> num;
        for (int i = 0; i < num; i++)
        {
            cin >> a[i];
        }
        cout << Kadane(a, num, &start, &end) << " " << start << " " << end << endl;
    }
}

int Kadane(int a[], int n, int *start, int *end)
{
    int i, j;
    int maxSum = 0, thisSum = 0;

    for (i = 0, j = 0; j < n; j++)
    {
        thisSum += a[j];
        if (thisSum > maxSum)
        {
            maxSum = thisSum;
            *start = i;
            *end = j;
        }
        else if (thisSum <= 0)
        {
            i = j + 1;
            thisSum = 0;
        }
    }
    return maxSum;
}