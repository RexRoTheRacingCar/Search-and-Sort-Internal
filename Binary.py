def binarySearch(arr, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l) // 2
        print("Array Element ", mid)
 
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
            
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
 
    # If we reach here, then the element
    # was not present
    return -1
 
 
# Code
if __name__ == '__main__':
    arr = [1, 7, 12, 14, 16, 22, 38, 44, 47, 51, 56, 58, 59, 69, 76, 82, 84, 96, 99, 100]
    x = 22

    print("Array - ", arr)
    print("Key Number", x)
    print("Array Length - ", len(arr))
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
