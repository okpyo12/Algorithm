#include <iostream>

using namespace std;

#define MAX_SIZE 100

int MCSS(int v[], int low, int high);
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        int num, value, a[MAX_SIZE];
        cin >> num;
        for (int i = 0; i < num; i++)
        {
            cin >> a[i];
        }
        cout << MCSS(a, 0, num - 1) << endl;
    }
}

int MCSS(int v[], int low, int high)
{
    int mid, ans;
    if (low == high)
    {
        return v[low];
    }
    mid = (low + high) / 2;
    int sum = 0;
    int left = -10000;
    int right = -10000;
    for (int i = mid; i >= low; i--)
    {
        sum += v[i];
        left = max(left, sum);
    }
    sum = 0;
    for (int i = mid + 1; i <= high; i++)
    {
        sum += v[i];
        right = max(right, sum);
    }
    ans = max(MCSS(v, low, mid), MCSS(v, mid + 1, high));
    int result = max(left + right, ans);
    if (result < 0)
    {
        return 0;
    }
    else
    {
        return result;
    }
    cout << result << endl;
}