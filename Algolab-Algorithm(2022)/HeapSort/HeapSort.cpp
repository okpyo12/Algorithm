#include <iostream>

using namespace std;

#define MAX_LENGTH 2000

int arr[MAX_LENGTH];
int swaped;
void HeapSort(int root, int k, int n);
void printArray(int arr[], int num)
{
    for (int i = 0; i < num; i++)
        cout << arr[i] << " ";
    cout << endl;
}
int main()
{
    int numTestCase;
    cin >> numTestCase;
    for (int i = 0; i < numTestCase; i++)
    {
        int num;
        cin >> num;
        swaped = 0;
        for (int j = 0; j < MAX_LENGTH; j++)
        {
            arr[j] = 0;
        }
        int idx = 0;
        for (int j = 1; j <= num; j++)
        {
            idx += 1;
            cin >> arr[j];
        }
        for (int j = num / 2; j >= 1; j--)
        {
            HeapSort(j, arr[j], num);
        }
        for (int j = num; j >= 2; j--)
        {
            int temp = arr[1];
            HeapSort(1, arr[j], j - 1);
            arr[j] = temp;
        }
        cout << swaped << endl;
    }
}

void HeapSort(int root, int k, int n)
{
    int vacant = root;
    int largeChild;

    while ((arr[vacant * 2] != 0 && vacant * 2 <= n) || (arr[vacant * 2 + 1] != 0 && vacant * 2 + 1 <= n))
    {
        if (arr[vacant * 2 + 1] != 0 && vacant * 2 + 1 <= n)
        {
            swaped = swaped + 2;
            if (arr[vacant * 2] > arr[vacant * 2 + 1])
            {
                largeChild = vacant * 2;
            }
            else
            {
                largeChild = vacant * 2 + 1;
            }
        }
        else
        {
            swaped++;
            largeChild = vacant * 2;
        }
        if (k < arr[largeChild])
        {
            arr[vacant] = arr[largeChild];
            vacant = largeChild;
        }
        else
        {
            break;
        }
    }
    arr[vacant] = k;
}