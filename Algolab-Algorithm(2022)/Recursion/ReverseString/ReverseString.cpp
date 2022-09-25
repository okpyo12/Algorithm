#include <iostream>
#include <string>

using namespace std;

string ReverseString(string a, int i, int j);
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        string a;
        cin >> a;
        int len = a.length();
        cout << ReverseString(a, 0, len - 1) << endl;
    }
}

string ReverseString(string a, int i, int j)
{
    if (i < j)
    {
        char temp;
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
        return ReverseString(a, i + 1, j - 1);
    }
    else
    {
        return a;
    }
}