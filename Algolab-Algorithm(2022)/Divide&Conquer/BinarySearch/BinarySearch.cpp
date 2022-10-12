#include <iostream>

using namespace std;

#define MAX_SIZE 100

int BinarySearch(int a[], int left, int right, int value);
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        int num, value, a[MAX_SIZE], left, right;
        cin >> num >> value;
        for (int i = 0; i < num; i++)
        {
            cin >> a[i];
        }
        cout << BinarySearch(a, 0, num - 1, value) << endl;
    }
}

int BinarySearch(int a[], int left, int right, int value)
{
    int mid;

    if (left > right)
    {
        return -1;
    }
    else
    {
        mid = (left + right) / 2;
        if (a[mid] == value)
        {
            return mid;
        }
        else if (a[mid] > value)
        {
            return BinarySearch(a, left, mid - 1, value);
        }
        else
        {
            return BinarySearch(a, mid + 1, right, value);
        }
    }
}