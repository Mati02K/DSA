public class SelectionSort 
{

    void selectionsort(int arr[])
    {
        int n = arr.length;

        for(int i=0; i<n-1; i++)
        {
            int temp = 0;

            for(int j=i+1; j<n-1;j++)
            {
                if(arr[i]>arr[j])
                {
                    temp = arr[j];
                    arr[j]=arr[i];
                    arr[i]=temp;
                    
                }
            }
        }
    }




    public static void main(String[] args) {

        int testarray[] = {64, 34, 25, 12, 22, 11, 90};
        SelectionSort s = new SelectionSort();
        s.selectionsort(testarray);
        System.out.println(testarray[0]);
        for(int k =0; k<testarray.length; k++)
        {
            System.out.println(testarray[k]);
        }
    }
    
}
