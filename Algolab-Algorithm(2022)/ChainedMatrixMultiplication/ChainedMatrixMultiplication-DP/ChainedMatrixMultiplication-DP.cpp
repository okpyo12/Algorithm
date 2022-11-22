#include <iostream>

using namespace std;

#define MAX_LENGTH 101

int DP[MAX_LENGTH][MAX_LENGTH];
int m[MAX_LENGTH][MAX_LENGTH];

void MatrixChain_Recursion(int matrix[], int num);
void order(int i, int j);
int main()
{
    int numTestCase;
    cin >> numTestCase;
    for (int i = 0; i < numTestCase; i++)
    {
        int num;
        cin >> num;
        int matrix[MAX_LENGTH];
        for (int j = 0; j < num + 1; j++)
        {
            cin >> matrix[j];
        }
        MatrixChain_Recursion(matrix, num + 1);
        order(1, num);
        cout << endl;
        cout << DP[1][num] << endl;
    }
}

void MatrixChain_Recursion(int matrix[], int num)
{
    for (int i = 1; i < num; i++)
    {
        DP[i][i] = 0;
    }
    for (int L = 2; L < num; L++)
    {
        for (int i = 1; i < num - L + 1; i++)
        {
            int j = i + L - 1;
            DP[i][j] = 987654321;
            for (int k = i; k < j; k++)
            {
                if (DP[i][j] > (DP[i][k] + DP[k + 1][j] + matrix[i - 1] * matrix[k] * matrix[j]))
                {
                    m[i][j] = k;
                }
                int q = DP[i][k] + DP[k + 1][j] + matrix[i - 1] * matrix[k] * matrix[j];
                if (q < DP[i][j])
                {
                    DP[i][j] = q;
                }
            }
        }
    }
}

void order(int i, int j)
{
    if (i == j)
    {
        cout << "M" << i;
    }
    else
    {
        int k = m[i][j];
        cout << "(";
        order(i, k);
        order(k + 1, j);
        cout << ")";
    }
}