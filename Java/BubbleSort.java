public class BubbleSort {

       void bubblesort(int arr[])
        {
            int n = arr.length;
            for(int i=0; i<n; i++)
            {
                for(int j=0; j<n-i-1; j++)
                {
                    // Here Comparing if the next variable is greater or not
                    if(arr[j]>arr[j+1])
                    {
                        int temp = arr[j];
                        arr[j] = arr[j+1];
                        arr[j+1] = temp;
                    }
                }
            }
        }


        public static void main(String[] args) 
        {
            BubbleSort b = new BubbleSort();
            int arr[] = {64, 34, 25, 12, 22, 11, 90};
            b.bubblesort(arr);
            for(int k=0;k<arr.length;k++)
            {
                System.out.println(arr[k]);
            }
           

        }
    
}
