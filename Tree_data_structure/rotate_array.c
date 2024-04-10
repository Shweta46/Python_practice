#include <stdio.h>
void swap(int* x, int* y) {
    int temp = *x;
    x = y;
    *y = temp;
}
void reverse(int arr[], int l, int r) {
    int i = l, j = r;
    while(i < j) {
        swap(&arr[i++], &arr[j--]);
    }
}
int main()
{
    int n, k;
    scanf("%d %d", &n, &k);

    k %= n;

    int arr[n];
    for(int i = 0 ; i < n ; i++) {
        scanf("%d", &arr[i]);
    }

    reverse(arr, 0, n - 1);
    reverse(arr, 0, n - k - 1);
    reverse(arr, n - k, n - 1);

    for(int i = 0 ; i < n ; i++) {
        printf("%d ", arr[i]);
    }
}