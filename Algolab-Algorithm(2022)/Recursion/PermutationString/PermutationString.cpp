#include <iostream>
#include <string>

using namespace std;

int cnt = 0;

void PermutationString(string a, int i, int j);
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        string a;
        cin >> a;
        int len = a.length();
        PermutationString(a, 0, len);
        cout << cnt << endl;
        cnt = 0;
    }
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void PermutationString(string a, int begin, int end)
{
    int range = end - begin;
    if (range == 1)
    {
        int w = 0;
        for (int j = 0; j < a.length(); j++)
        {
            if (j % 2 == 0)
            {
                w += int(a[j]) - 97;
            }
            else
            {
                w -= int(a[j]) - 97;
            }
        }
        if (w > 0)
        {
            cnt++;
        }
    }
    else
    {
        for (int i = 0; i < range; i++)
        {
            swap(a[begin], a[begin + i]);
            PermutationString(a, begin + 1, end);
            swap(a[begin], a[begin + i]);
        }
    }
}