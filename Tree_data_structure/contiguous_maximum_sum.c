#include<stdio.h>
int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for(int i = 0 ; i < n ; i++) {
        scanf("%d", &arr[i]);
    }

    int curr = 0, mx = 0;
    int flag = 1;
    int l = 0, r = 0;

    for(int i = 0 ; i < n ; i++) {
        if(arr[i] > 0)
            flag = 0;
        curr += arr[i];
        if(curr < 0) 
            curr = 0;
        if(curr > mx)
            mx = curr;
    }

    if(flag == 1) {
        int m = -999999;
        for(int i = 0 ; i < n ; i++) {
            if(arr[i] > m)
                m = arr[i];
        }
        printf("%d ", m);
        return 0;
    }

    printf("%d", mx);
}