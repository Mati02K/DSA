/* Java program for Merge Sort */
class MergeSort
{

    void merge(int arr[],int f,int m, int l)
    {
        // Lets Calculate the length of two Arrays:
        int n1 = m - f + 1;
        int n2 = l - m;

        // Creating Two Temp Arrays
        int L[] = new int[n1];
        int R[] = new int[n2];

        // Copy Data 
        for(int i = 0;i<n1;++i)
        {
            L[i] = arr[f+i];
        }
        for(int j=0;j<n2;++j)
        {
            R[j] = arr[m+1+j];
        }

        // Perform Merge Step
        int i=0;
        int j = 0;
        
        int k=f;
        while(i < n1 && j < n2)
        {
            if(L[i] <= R[j])
            {
                arr[k]=L[i];
                i++;
            }
            else
            {
                arr[k]=R[j];
                j++;
            }
            k++;
        }
        
        /* Copy remaining elements of L[] if any */
        // while (i < n1) {
        //     arr[k] = L[i];
        //     i++;
        //     k++;
        // }
 
        /* Copy remaining elements of R[] if any */
        // while (j < n2) {
        //     arr[k] = R[j];
        //     j++;
        //     k++;
        // }
    }

	public void sort(int arr[],int first,int last)
    {
     //  int middle = (first+last)/2; You Should not get the middle value through this format
     if(first < last)
     {
     int middle = first + (last-first)/2;

    //  Sorting by breaking the arrays
     sort(arr,first,middle);
     sort(arr,middle+1,last);

    //  Now Lets Call Merge Sort
    
     merge(arr, first, middle, last);
     }
    }

    static void printArray(int arr[])
    {
        for(int i=0; i<arr.length;i++)
        {
            System.out.println(arr[i]);
        }
    }

	// Driver code
	public static void main(String args[])
	{
		int arr[] = { 12, 11, 13, 5, 6, 7 };

		System.out.println("Given Array");
		printArray(arr);

		MergeSort ob = new MergeSort();
		ob.sort(arr, 0, arr.length - 1);

		System.out.println("\nSorted array");
		printArray(arr);
	}
}
