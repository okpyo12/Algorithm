#include <iostream>

using namespace std;

int FastFibonacci(int a);
void multi(int A[2][2], int B[2][2]);
void pow(int matrix[2][2], int num);

int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        int n;
        cin >> n;
        cout << FastFibonacci(n) % 1000 << endl;
    }
}

void multi(int A[2][2], int B[2][2])
{
    int mul[2][2];
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            mul[i][j] = 0;
            for (int k = 0; k < 2; k++)
            {
                mul[i][j] += A[i][k] * B[k][j] % 10000;
            }
        }
    }
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            A[i][j] = mul[i][j];
        }
    }
}

void pow(int matrix[2][2], int num)
{
    if (num <= 1)
    {
        return;
    }
    int M[2][2] = {{1, 1}, {1, 0}};
    pow(matrix, num / 2);
    multi(matrix, matrix);

    if (num % 2 != 0)
    {
        multi(matrix, M);
    }
}

int FastFibonacci(int n)
{
    int M[2][2] = {{1, 1}, {1, 0}};

    if (n <= 1)
    {
        return n;
    }
    else if (n == 2)
    {
        return 1;
    }
    else
    {
        pow(M, n - 1);
    }
    return M[0][0];
}