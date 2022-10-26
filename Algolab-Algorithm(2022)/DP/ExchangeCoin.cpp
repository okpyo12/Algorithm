#include <iostream>
using namespace std;

int dp[64];
int coin[5] = {1, 5, 10, 21, 25};

int main()
{
	int i, j;
	for (i = 1; i <= 63; i++)
	{
		dp[i] = 987654321;
	}
	for (i = 0; i < 5; i++)
	{
		cout << "동전 " << coin[i] << " 사용 시" << endl;
		for (j = coin[i]; j <= 63; j++)
		{
			dp[j] = min(dp[j], dp[j - coin[i]] + 1);
			cout << "j : " << j << " "
				 << "dp[j]: " << dp[j] << endl;
		}
	}
	cout << dp[63] << endl;
	for (int i = 0; i < 64; i++)
	{
		cout << dp[i] << endl;
	}
}