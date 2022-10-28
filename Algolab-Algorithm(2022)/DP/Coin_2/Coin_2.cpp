#include <iostream>

using namespace std;

#define MIN(a, b) ((a) < (b) ? (a) : (b))

int a[101] = {};
int dp[10001] = {};

int coin_2(int n, int k);
int main()
{
    int n, k;
    cin >> n;
    cin >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    cout << coin_2(n, k) << endl;
}

int coin_2(int n, int k)
{
    for (int i = 1; i <= k; i++)
    {
        dp[i] = 100001;
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = a[i]; j <= k; j++)
        {
            dp[j] = MIN(dp[j], dp[j - a[i]] + 1);
        }
    }
    if (dp[k] == 100001)
    {
        return -1;
    }
    else
    {
        return dp[k];
    }
}