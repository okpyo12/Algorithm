#include <iostream>

using namespace std;

#define MAX_SIZE 100

int FindingMax(int a[], int left, int right);
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        int num, a[MAX_SIZE], left, right;
        cin >> num;
        for (int i = 0; i < num; i++)
        {
            cin >> a[i];
        }
        cout << FindingMax(a, 0, num - 1) << endl;
    }
}

int FindingMax(int a[], int left, int right)
{
    int half;

    if (left == right)
    {
        return a[left];
    }
    else
    {
        half = (left + right) / 2;
        return max(FindingMax(a, left, half), FindingMax(a, half + 1, right));
    }
}