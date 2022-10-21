#include <iostream>

using namespace std;

#define MAX_SIZE 1000

void swap(int *a, int *b);
void quicksort_Hoare(int a[], int low, int high);
int partition_Hoare(int a[], int low, int high);
void quicksort_Lomuto(int a[], int low, int high);
int partition_Lomuto(int a[], int low, int high);
int swapH = 0;
int swapL = 0;
int comparionH = 0;
int comparionL = 0;
int main()
{
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i)
    {
        int num, a[MAX_SIZE], b[MAX_SIZE];
        cin >> num;
        for (int j = 0; j < num; j++)
        {
            cin >> a[j];
            b[j] = a[j];
        }
        quicksort_Hoare(a, 0, num - 1);
        quicksort_Lomuto(b, 0, num - 1);
        cout << swapH << " " << swapL << " " << comparionH << " " << comparionL << endl;
        swapH = 0, swapL = 0, comparionH = 0, comparionL = 0;
    }
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void quicksort_Hoare(int a[], int low, int high)
{
    if (low >= high)
    {
        return;
    }
    int p = partition_Hoare(a, low, high);
    quicksort_Hoare(a, low, p);
    quicksort_Hoare(a, p + 1, high);
}

int partition_Hoare(int a[], int low, int high)
{
    int pivot = a[low];
    int i = low - 1;
    int j = high + 1;

    while (true)
    {
        do
        {
            i++;
            comparionH++;
        } while (a[i] < pivot);
        do
        {
            j--;
            comparionH++;
        } while (a[j] > pivot);
        if (i < j)
        {
            swapH++;
            swap(&a[i], &a[j]);
        }
        else
        {
            return j;
        }
    }
}

void quicksort_Lomuto(int a[], int low, int high)
{
    if (low >= high)
    {
        return;
    }
    int p = partition_Lomuto(a, low, high);
    quicksort_Lomuto(a, low, p - 1);
    quicksort_Lomuto(a, p + 1, high);
}

int partition_Lomuto(int a[], int low, int high)
{
    int pivot = a[low];
    int j = low;
    for (int i = low + 1; i <= high; i++)
    {
        comparionL++;
        if (a[i] < pivot)
        {
            j++;
            swapL++;
            swap(&a[i], &a[j]);
        }
    }
    int pivot_pos = j;
    swapL++;
    swap(&a[pivot_pos], &a[low]);
    return pivot_pos;
}
