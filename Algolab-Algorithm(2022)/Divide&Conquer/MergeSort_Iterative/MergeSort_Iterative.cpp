#include <iostream>

using namespace std;

#define MAX_SIZE 1000

void MergeSortIterative(int v[], int n);
void Merge(int a[], int low, int mid, int high);
int cnt = 0;
int main()
{
    int numTestCase;
    cin >> numTestCase;
    for (int i = 0; i < numTestCase; i++)
    {
        int num, a[MAX_SIZE];
        cin >> num;
        for (int j = 0; j < num; j++)
        {
            cin >> a[j];
        }
        MergeSortIterative(a, num);
        cout << cnt << endl;
        cnt = 0;
    }
}

void MergeSortIterative(int v[], int n)
{
    int size = 1;
    while (size < n)
    {
        for (int i = 0; i < n; i += 2 * size)
        {
            int low = i;
            int mid = low + size - 1;
            int high = min(i + 2 * size - 1, n - 1);
            if (mid >= n - 1)
            {
                break;
            }
            Merge(v, low, mid, high);
        }
        size *= 2;
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
        cnt++;
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