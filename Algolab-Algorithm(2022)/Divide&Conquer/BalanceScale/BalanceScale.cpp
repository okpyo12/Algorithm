#include <iostream>

using namespace std;

#define MAX_SIZE 10000

int BalanceScale(int a[], int num);
int main()
{
    int numTestCase;
    cin >> numTestCase;
    for (int i = 0; i < numTestCase; i++)
    {
        int num, a[MAX_SIZE];
        cin >> num;
        for (int j = 0; j < num; j++)
        {
            cin >> a[j];
        }
        cout << BalanceScale(a, num) << endl;
    }
}

int BalanceScale(int a[], int num)
{
    int left = 0;
    int right = 0;
    int w[7] = {100, 50, 20, 10, 5, 2, 1};
    int idx = 0;
    for (int i = 0; i < num; i++)
    {
        if (left == right)
        {
            left += a[i];
        }
        else if (left > right)
        {
            right += a[i];
        }
        else if (left < right)
        {
            left += a[i];
        }
    }
    int gap = 0;
    if (right > left)
    {
        gap = right - left;
    }
    else if (left > right)
    {
        gap = left - right;
    }
    else
    {
        return 0;
    }
    int cnt = 0;
    for (int i = 0; i < 7; i++)
    {
        if (gap / w[i] > 0)
        {
            cnt += gap / w[i];
            gap = gap % w[i];
        }
    }
    return cnt;
}