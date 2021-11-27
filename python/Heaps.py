'''
Heap is one of the Data Structure  where elements are arranged based on minimum or maximum element placed in the node.
MIN HEAP - The node element is the minimum
MAX HEAP - The node element is the maximum
Mostly we take heap as MAX HEAP and process of converting a normal array to heap is called Heapify
The heap is represented in form of array with below conditions
1) When parent is at i , the leftchild will be at 2i + 1, and right child will be at 2i + 2
2) If child is at i, the parent is at [i/2] - 1
3) Leaves node ranges from N/2 ---> N-1 (N denotes total no of elements in an array)
4) Internal Nodes ranges from( 0 -----> [N/2] - 1)

Note: The main two conitions for the input to Heap is given below
	i) The tree should be complete Binary tree
	ii) Half Complete(Leaves(last level) at same level must be filled from left to right)
'''

# Process to (MAX)heapify the array Time complexity is O(logn)  (Can be also called max priority queue)
def heapify(arr,index,length):
	left = (2 * index) + 1
	right = (2 * index) + 2
	largest = index # Setting the current index as the largest
	if(left < length and arr[left] > arr[index]):
		largest = left
	if(right < length and arr[right] > arr[largest]):
		largest = right
	if largest != index:
		arr[index],arr[largest] = arr[largest],arr[index]
		heapify(arr,largest,length)

# When given a array try to heapify from below and swap based
def heapsort(arr):
	n = len(arr)

# 	Building a MAX HEAP
	for i in range((n//2)- 1,-1,-1):
		heapify(arr,i,n)

	for i in range(n-1,0,-1):
		arr[0],arr[i] = arr[i],arr[0]
		heapify(arr,0,i) # Since after i indexed elements have been sorted we have to heapify the elements only below i.

if __name__ == '__main__':
	arr = [4, 10, 3, 5, 1]
	#heapify(arr,0,len(arr))
	heapsort(arr)
	print(arr)

