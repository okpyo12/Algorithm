#include <iostream>

using namespace std;

#define MAX_LENGTH 101
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int L[MAX_LENGTH][MAX_LENGTH], S[MAX_LENGTH][MAX_LENGTH];

int LCS_Memo(char s[], char t[], int m, int n);
int main()
{
    int numTestCase;
    cin >> numTestCase;
    for (int i = 0; i < numTestCase; i++)
    {
        char s[MAX_LENGTH], t[MAX_LENGTH];
        cin >> s;
        cin >> t;
        int m, n;
        for (m = 0; s[m] != 0;)
        {
            m++;
        }
        for (n = 0; t[n] != 0;)
        {
            n++;
        }
        for (int i = 0; i < MAX_LENGTH; i++)
        {
            for (int j = 0; j < MAX_LENGTH; j++)
            {
                L[i][j] = -1;
            }
        }
        cout << LCS_Memo(s, t, m, n) << endl;
    }
}

int LCS_Memo(char s[], char t[], int m, int n)
{
    if (m == 0 || n == 0)
    {
        return 0;
    }
    if (L[m][n] < 0)
    {
        if (s[m - 1] == t[n - 1])
        {
            L[m][n] = LCS_Memo(s, t, m - 1, n - 1) + 1;
            return L[m][n];
        }
        L[m][n] = MAX(LCS_Memo(s, t, m - 1, n), LCS_Memo(s, t, m, n - 1));
    }
    return L[m][n];
}