public class InsertionSort {

    void insertionsort(int arr[])
    {
        int n = arr.length;

        for(int i=0; i<n; ++i)
        {
            int key = arr[i];
            int j = i-1;

            // Checking upto Current Array is sorted
            while(j>=0 && arr[j]>key)
            {
                arr[j+1] = arr[j];
                j = j-1;
            }
            arr[j+1] = key;
        }
    }
    
    public static void main(String[] args) 
    {
        int testarray[] = {64, 34, 25, 12, 22, 11, 90};
        InsertionSort i = new InsertionSort();
        i.insertionsort(testarray);

        for(int k=0; k<testarray.length; k++)
        {
            System.out.println(testarray[k]);
            
        }
        
    }
    
}
