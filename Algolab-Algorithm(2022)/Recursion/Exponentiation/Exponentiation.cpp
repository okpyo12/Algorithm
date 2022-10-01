#include <iostream>

using namespace std;

int Exponentiation(int a, int b);
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        int a, b;
        cin >> a >> b;
        cout << Exponentiation(a, b) << endl;
    }
}

int Exponentiation(int a, int b)
{
    int num;
    if (b == 0)
    {
        return 1;
    }
    else if (b % 2 == 1)
    {
        num = Exponentiation(a, (b - 1) / 2);
        return (a * num * num) % 1000;
    }
    else
    {
        num = Exponentiation(a, b / 2);
        return (num * num) % 1000;
    }
}