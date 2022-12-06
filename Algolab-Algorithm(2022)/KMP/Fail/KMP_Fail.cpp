#include <iostream>

using namespace std;

#define MAX_SIZE 1001

int patLength, txtLength;
int fail[MAX_SIZE];
int KMP(char text[], char pattern[]);
void getFail(char pattern[]);
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
            fail[i] = 0;
        }
        getFail(pattern);
        for (int i = 0; i < patLength; i++)
        {
            cout << fail[i] << " ";
        }
        cout << endl;
        cout << KMP(text, pattern) << endl;
    }
}

int KMP(char text[], char pattern[])
{
    int j = 0;
    int ans = 0;
    for (int i = 0; i < txtLength; i++)
    {
        while (j > 0 && text[i] != pattern[j])
        {
            j = fail[j - 1];
        }
        if (text[i] == pattern[j])
        {
            if (j == patLength - 1)
            {
                ans++;
                j = fail[j];
            }
            else
            {
                j++;
            }
        }
    }
    return ans;
}

void getFail(char pattern[])
{
    int j = 0;
    for (int i = 1; i < patLength; i++)
    {
        while (j > 0 && pattern[i] != pattern[j])
        {
            j = fail[j - 1];
        }
        if (pattern[i] == pattern[j])
        {
            fail[i] = ++j;
        }
    }
}