#include <stdio.h>
#include <stdlib.h>

int candy(int* ratings, int ratingsSize){
    int i = 0;
    int totalCandy = 0;
    int * past = NULL;
    int * cur = NULL;
    int *left2right = NULL;
    int *right2left = NULL;
    if (ratingsSize == 1){
        return 1;
    }
                    
    left2right = (int*) malloc(sizeof(int)* ratingsSize);
    if (left2right == NULL){
        return -1;
    }
    right2left = (int *)malloc(sizeof(int) * ratingsSize);
    if (NULL == right2left ){
        free(left2right);
        return -1;
    }
    
    past = ratings;
    left2right[0] = 1;
    for (i = 1; i <ratingsSize; i++){
        cur = ratings + i;
        if (*past < *cur){
            left2right[i] = left2right[i-1] + 1;
        }
        else{
            left2right[i] = 1;
        }
        past = cur;
    }
    right2left[ratingsSize-1] = 1;
    for (i = ratingsSize-2;i>=0;i--){
        cur = ratings + i;
        if (* cur > *past){
            right2left[i] = right2left[i+1] + 1;
        }
        else{
            right2left[i] = 1;
        }
        past = cur;
    }
    
    for(i = 0; i< ratingsSize; i++){
        totalCandy += left2right[i] > right2left[i] ? left2right[i] : right2left[i]; 
    }
    free(left2right);
    free(right2left);
        
    return totalCandy;
}