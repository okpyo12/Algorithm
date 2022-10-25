#include <iostream>

using namespace std;

int a[101] = {};
int dp[10001] = {};

int coin_1(int n, int k);
int main()
{
    int n, k;
    cin >> n;
    cin >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    cout << coin_1(n, k) << endl;
}

int coin_1(int n, int k)
{
    dp[0] = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = a[i]; j <= k; j++)
        {
            if (dp[j - a[i]])
            {
                dp[j] += dp[j - a[i]];
            }
        }
    }
    return dp[k];
}