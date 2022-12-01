#include <iostream>

using namespace std;

int num;
int answer = 0;
int col[16];

void NQueen(int row);
int isPromising(int row);
int main()
{
    int numTestCase;
    cin >> numTestCase;
    for (int i = 0; i < numTestCase; i++)
    {
        cin >> num;
        for (int j = 0; j < num; j++)
        {
            col[0] = j;
            NQueen(0);
        }
        answer = 0;
    }
}

void NQueen(int row)
{
    if (answer == 1)
    {
        return;
    }
    if (isPromising(row))
    {
        if (row == num - 1)
        {
            for (int i = 0; i < num; i++)
            {
                cout << col[i] + 1 << " ";
            }
            cout << endl;
            answer = 1;
        }
        else
        {
            for (int i = 0; i < num; i++)
            {
                col[row + 1] = i;
                NQueen(row + 1);
            }
        }
    }
}

int isPromising(int row)
{
    int k = 0;
    int promising = 1;
    while (k < row && promising)
    {
        if (col[row] == col[k] || abs(col[row] - col[k]) == row - k)
        {
            promising = 0;
        }
        k++;
    }
    return promising;
}