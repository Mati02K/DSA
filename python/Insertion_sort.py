from util import time_it

@time_it
def insertion_sort(elements):
    for i in range(len(elements)-1):
        j = i + 1
        while j > 0:
            if elements[j-1] > elements[j]:
                #Swap
                elements[j-1],elements[j] = elements[j],elements[j-1]
            else:
                # Since the array is sorted just break to save some time
                break
            j-=1

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)
    
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')