import random

def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]

        j = i - 1

        print("Key - ", key_item, " | iteration - ", i)

        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

        if key_item < array[i-1]:
            print("Lowered Item")
        else:
            print("Item not moved")

    return array

def binarySearch(array, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l) // 2
        print("Array Element ", mid)
 
        # Check if x is present at mid
        if array[mid] == x:
            return mid
            
 
        # If x is greater, ignore left half
        elif array[mid] < x:
            l = mid + 1

 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
 
    # If we reach here, then the element
    # was not present
    return -1

def linearSearch(array, n, x):
 
    for i in range(0, n):
        print("Array Element ", array[i])
        if (array[i] == x):
            return i
    return -1

if __name__ == '__main__':

    import random
    
    array =[]

    for i in range(10):

       r=random.randint(1,1000)
 
       if r not in array:
                   array.append(r)

    print("Array - ", array)
    print("Array Length - ", len(array))
        
    # Function call
    insertion_sort(array)

    print("Sorted Array - ", array)

    x = random.choice(array)

    print("Array - ", array)
    print("Key Number", x)
    print("Array Length - ", len(array))
    
    # Function call
    #result = binarySearch(array, 0, len(array)-1, x)

    result = linearSearch(array, len(array)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")



