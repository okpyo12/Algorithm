#include <iostream>

using namespace std;

#define MAX_SIZE 100

void MergeSort(int v[], int low, int high);
void Merge(int a[], int low, int mid, int high);
int cnt = 0;
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        int num, value, a[MAX_SIZE];
        cin >> num;
        for (int i = 0; i < num; i++)
        {
            cin >> a[i];
        }
        MergeSort(a, 0, num - 1);
        cout << cnt << endl;
        cnt = 0;
    }
}

void Merge(int a[], int low, int mid, int high)
{
    int i, j, k;
    int tmp[MAX_SIZE];

    for (i = low; i <= high; i++)
    {
        tmp[i] = a[i];
    }

    i = k = low;
    j = mid + 1;
    while (i <= mid && j <= high)
    {
        cnt += 1;
        if (tmp[i] <= tmp[j])
        {
            a[k++] = tmp[i++];
        }
        else
        {
            a[k++] = tmp[j++];
        }
    }
    while (i <= mid)
    {
        a[k++] = tmp[i++];
    }
    while (j <= high)
    {
        a[k++] = tmp[j++];
    }
}

void MergeSort(int v[], int low, int high)
{
    int mid;
    if (low == high)
    {
        return;
    }
    mid = (low + high) / 2;

    MergeSort(v, low, mid);
    MergeSort(v, mid + 1, high);
    Merge(v, low, mid, high);
}