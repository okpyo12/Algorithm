#include <iostream>

using namespace std;

#define MAX_SIZE 1001

int patLength, txtLength, ZX, CV;
int DFA[MAX_SIZE][MAX_SIZE];
void constructDFA(char pattern[]);
void KMP(char text[]);
int main()
{
    int numTestCase;
    cin >> numTestCase;
    for (int i = 0; i < numTestCase; i++)
    {
        string a, b;
        cin >> a >> b;
        patLength = 0;
        txtLength = 0;
        ZX = 1;
        CV = 0;
        char pattern[MAX_SIZE];
        char text[MAX_SIZE];
        for (int i = 0; a[i] != 0; i++)
        {
            pattern[i] = a[i];
            patLength++;
        }
        for (int i = 0; b[i] != 0; i++)
        {
            text[i] = b[i];
            txtLength++;
        }
        for (int i = 0; i < MAX_SIZE; i++)
        {
            for (int j = 0; j < MAX_SIZE; j++)
            {
                DFA[i][j] = 0;
            }
        }
        constructDFA(pattern);
        KMP(text);
        cout << ZX << " " << CV << endl;
    }
}

void KMP(char text[])
{
    for (int i = 0, j = 0; i < txtLength; i++)
    {
        j = DFA[text[i]][j];
        if (j == patLength)
        {
            CV++;
        }
    }
}

void constructDFA(char pattern[])
{
    DFA[pattern[0]][0] = 1;
    for (int i = 0, j = 1; j <= patLength; j++)
    {
        for (int k = 0; k < 3; k++)
        {
            char pat;
            if (k == 0)
            {
                pat = 'A';
            }
            else if (k == 1)
            {
                pat = 'B';
            }
            else
            {
                pat = 'C';
            }
            DFA[pat][j] = DFA[pat][i];
            if (DFA[pat][j] != 0)
            {
                ZX++;
            }
        }
        if (j < patLength)
        {
            if (DFA[pattern[j]][j] == 0)
            {
                ZX++;
            }
            DFA[pattern[j]][j] = j + 1;
            i = DFA[pattern[j]][i];
        }
    }
}