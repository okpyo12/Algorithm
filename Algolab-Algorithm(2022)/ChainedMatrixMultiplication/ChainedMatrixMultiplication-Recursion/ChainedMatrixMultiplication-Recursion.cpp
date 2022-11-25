#include <iostream>

using namespace std;

#define MAX_LENGTH 101
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int MatrixChain_Recursion(int matrix[], int start, int end);
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
        cout << MatrixChain_Recursion(matrix, 1, num) << endl;
    }
}

int MatrixChain_Recursion(int matrix[], int start, int end)
{
    if (start == end)
        return 0;
    int m = 987654321;

    for (int i = start; i < end; i++)
    {
        int temp = MatrixChain_Recursion(matrix, start, i) + MatrixChain_Recursion(matrix, i + 1, end) + (matrix[start - 1] * matrix[i] * matrix[end]);
        m = MIN(m, temp);
    }
    return m;
}