from util import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)



def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

# Find Peak Element in an Array
def findPeak(arr):
    if len(arr) == 1:
        return arr[0]

    left = arr[0]
    right = arr[-1]

    if right > left: # Array is sorted in ascending order and not rotated
        return right

    if left > arr[1]: # Array is sorted in descending order and not rotated
        return left

    # Array is rotated sorted then proceed to find the peak element
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2
        if mid + 1 <= end and arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return arr[mid]
        elif arr[mid] < arr[mid-1]:
            return arr[mid-1]
        elif arr[mid] > right:  # If my mid element is greater than last element then the element is in the first half of the array,(i.e befor peak)
            start= mid+1
        else: # Else my element is after peak portion
            end = mid-1

    return arr[start]
    

if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 24

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using Linear search")

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using binary search")

    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    numbers_to_find = 15  
    print(find_all_occurances(numbers,numbers_to_find))
    print("{number_to_find} is found in",find_all_occurances(numbers,numbers_to_find))

    elements = [
        [1, 2],
        [11, 12, 13, 14, 15, 16, 10, 9, 8],
        [1],
        [2, 3, 4],
        [3, 1, 2],
        [25, 24, 23, 22, 21, 20]
    ]
    for element in elements:
        print(findPeak(element))
