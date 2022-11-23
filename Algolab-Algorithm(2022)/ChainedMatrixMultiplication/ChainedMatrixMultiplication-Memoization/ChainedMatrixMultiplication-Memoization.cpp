#include <iostream>

using namespace std;

#define MAX_LENGTH 101
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int dp[MAX_LENGTH][MAX_LENGTH];

int MatrixChain_Memo(int matrix[], int start, int end);
int main()
{
    int numTestCase;
    cin >> numTestCase;
    for (int i = 0; i < numTestCase; i++)
    {
        int num;
        cin >> num;
        int matrix[MAX_LENGTH];
        for (int i = 0; i < MAX_LENGTH; i++)
        {
            for (int j = 0; j < MAX_LENGTH; j++)
            {
                dp[i][j] = -1;
            }
        }
        for (int j = 0; j < num + 1; j++)
        {
            cin >> matrix[j];
        }
        cout << MatrixChain_Memo(matrix, 1, num) << endl;
    }
}

int MatrixChain_Memo(int matrix[], int start, int end)
{
    if (start == end)
    {
        return 0;
    }
    if (dp[start][end] != -1)
    {
        return dp[start][end];
    }

    dp[start][end] = 987654321;

    for (int i = start; i < end; i++)
    {
        dp[start][end] = MIN(dp[start][end], MatrixChain_Memo(matrix, start, i) + MatrixChain_Memo(matrix, i + 1, end) + matrix[start - 1] * matrix[i] * matrix[end]);
    }
    return dp[start][end];
}