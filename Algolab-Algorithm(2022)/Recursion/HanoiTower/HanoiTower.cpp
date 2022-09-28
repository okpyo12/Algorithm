#include <iostream>
#include <string>

#define MAX_SIZE 10
using namespace std;

int Array[MAX_SIZE] = {};
int idx = 0;

void HanoiTower(int n, int a, int b, int c);
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        int a;
        cin >> a;
        HanoiTower(a, 1, 2, 3);
        cout << "\n";
        for (int j = 0; j < MAX_SIZE; j++)
        {
            Array[j] = 0;
        }
        idx = 0;
    }
}

void HanoiTower(int n, int a, int b, int c)
{
    if (n > 0)
    {
        HanoiTower(n - 1, a, c, b);
        if (a == 3)
        {
            idx--;
            Array[idx] = 0;
            cout << Array[idx - 1] << " ";
        }
        else if (c == 3)
        {
            Array[idx] = n;
            cout << Array[idx] << " ";
            idx++;
        }
        HanoiTower(n - 1, b, a, c);
    }
}