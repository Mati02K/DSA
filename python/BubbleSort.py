from util import time_it
# you can use this to sort strings too
def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break
    
    return elements
@time_it
def bubble_sort_key(elements,key):
    search_list = []
    for i in range(len(elements)):
        temp_list = elements[i]
        search_list.append(temp_list[key])

    return bubble_sort(search_list)


if __name__ == '__main__':
    # elements = [5,9,2,1,67,34,88,34]
    # elements = [1,2,3,4,2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements)
    print(elements)

    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    print(bubble_sort_key(elements,'transaction_amount'))