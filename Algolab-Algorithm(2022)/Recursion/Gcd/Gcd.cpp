#include <iostream>

using namespace std;

int Gcd(int a, int b);
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        int a, b;
        cin >> a >> b;
        cout << Gcd(a, b) << endl;
    }
}

int Gcd(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    else
    {
        return Gcd(b, a % b);
    }
}