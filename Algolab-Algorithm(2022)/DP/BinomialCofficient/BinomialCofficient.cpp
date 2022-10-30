#include <iostream>

#define MAX 30
#define MIN(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

int binCoeff(int n, int k)
{
    int B[MAX][MAX] = {};
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= MIN(i, k); j++)
        {
            if (j == 0 || j == i)
            {
                B[i][j] = 1;
            }
            else
            {
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j];
            }
        }
    }
    return B[n][k];
}

int main()
{
    cout << binCoeff(7, 7) << endl;
}