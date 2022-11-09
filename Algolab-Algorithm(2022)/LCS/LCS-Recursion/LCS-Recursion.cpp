#include <iostream>

using namespace std;

#define MAX_LENGTH 11
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int L[MAX_LENGTH][MAX_LENGTH], S[MAX_LENGTH][MAX_LENGTH];

int LCS_Recursion(char s[], char t[], int m, int n);
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
        cout << LCS_Recursion(s, t, m, n) << endl;
    }
}

int LCS_Recursion(char s[], char t[], int m, int n)
{
    if (m == 0 || n == 0)
    {
        S[m][n] = 0;
        return S[m][n];
    }
    if (s[m - 1] == t[n - 1])
    {
        S[m][n] = LCS_Recursion(s, t, m - 1, n - 1) + 1;
        return S[m][n];
    }
    return max(LCS_Recursion(s, t, m - 1, n), LCS_Recursion(s, t, m, n - 1));
}