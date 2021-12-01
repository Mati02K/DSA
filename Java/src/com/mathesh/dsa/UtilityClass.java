package com.mathesh.dsa;

//This class consists of some of the utility functions like swap which can be used in other classes.

public class UtilityClass {

    public static int[] arrSlice(int[] arr, int start, int end){
        if(end > arr.length){
            end = (arr.length - 1) + 1;
        }
        int[] op = new int[end - start];
        int pos = 0;
        for(int i = start; i < end; i++){
            op[pos] = arr[i];
            pos ++;
        }
        return op;
    }
}
