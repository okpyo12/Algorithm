#include <iostream>

using namespace std;

#define MAX_LENGTH 101
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int L[MAX_LENGTH][MAX_LENGTH], S[MAX_LENGTH][MAX_LENGTH];
char arr[MAX_LENGTH];

int LCS_DP(char s[], char t[], int m, int n);

int main()
{
    int numTestCase;
    cin >> numTestCase;
    for (int i = 0; i < numTestCase; i++)
    {
        string q, p;
        cin >> q;
        cin >> p;
        int m = q.size();
        int n = p.size();
        int idx;
        char s[m];
        char t[n];
        for (int i = 0; i < m; i++)
        {
            s[i] = q[i];
        }
        for (int i = 0; i < n; i++)
        {
            t[i] = p[i];
        }
        for (int i = 0; i < max(m, n); i++)
        {
            arr[i] = '\0';
        }
        cout << LCS_DP(s, t, m, n) << " ";
        for (idx = 0; arr[idx] != 0;)
        {
            idx++;
        }
        for (idx = 0; arr[idx] != 0;)
        {
            idx++;
        }
        for (int i = idx; i >= 0; i--)
        {
            cout << arr[i];
        }
        cout << endl;
    }
}

int LCS_DP(char s[], char t[], int m, int n)
{
    for (int i = 0; i <= m; i++)
    {
        L[i][0] = 0;
    }
    for (int i = 0; i <= n; i++)
    {
        L[0][i] = 0;
    }
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (s[i - 1] == t[j - 1])
            {
                L[i][j] = L[i - 1][j - 1] + 1;
                S[i][j] = 0;
            }
            else
            {
                L[i][j] = MAX(L[i][j - 1], L[i - 1][j]);
                if (L[i][j] == L[i][j - 1])
                {
                    S[i][j] = 1;
                }
                else
                {
                    S[i][j] = 2;
                }
            }
        }
    }
    int idx = 0;
    for (int i = m; i >= 0;)
    {
        for (int j = n; j >= 0;)
        {
            if (L[i][j] == 0)
            {
                i = -1;
                j = -1;
                break;
            }
            if (s[i - 1] == t[j - 1])
            {
                arr[idx] = s[i - 1];
                idx++;
                i--;
                j--;
            }
            else
            {
                if (L[i][j] == L[i][j - 1])
                {
                    j--;
                }
                else
                {
                    i--;
                }
            }
        }
    }
    return L[m][n];
}