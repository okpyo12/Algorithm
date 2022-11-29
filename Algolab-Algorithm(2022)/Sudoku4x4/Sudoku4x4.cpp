#include <iostream>

using namespace std;

#define MAX_LENGTH 4
int board[MAX_LENGTH][MAX_LENGTH];
int answer = 0;

void Sudoku(int x, int y);
int isPromising(int x, int y, int a);
int main()
{
    int numTestCase;
    cin >> numTestCase;
    for (int i = 0; i < numTestCase; i++)
    {
        for (int j = 0; j < MAX_LENGTH; j++)
        {
            for (int k = 0; k < MAX_LENGTH; k++)
            {
                cin >> board[j][k];
            }
        }
        Sudoku(0, 0);
        answer = 0;
    }
}

void Sudoku(int x, int y)
{
    if (answer != 0)
    {
        return;
    }
    if (x == 4)
    {
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
        answer = 1;
        return;
    }
    if (y == 4)
    {
        Sudoku(x + 1, 0);
    }
    if (board[x][y] == 0)
    {
        for (int i = 1; i <= 4; i++)
        {
            if (isPromising(x, y, i))
            {
                board[x][y] = i;
                Sudoku(x, y + 1);
                board[x][y] = 0;
            }
        }
    }
    else
    {
        Sudoku(x, y + 1);
    }
}

int isPromising(int x, int y, int a)
{
    int promising = 0;
    for (int i = 0; i < 4; i++)
    {
        if (board[x][i] == a)
        {
            return promising;
        }
        if (board[i][y] == a)
        {
            return promising;
        }
    }
    for (int i = (x / 2) * 2; i < (x / 2) * 2 + 2; i++)
    {
        for (int j = (y / 2) * 2; j < (y / 2) * 2 + 2; j++)
        {
            if (board[i][j] == a)
            {
                return promising;
            }
        }
    }
    promising = 1;
    return promising;
}