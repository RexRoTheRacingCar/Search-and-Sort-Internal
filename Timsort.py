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

if __name__ == '__main__':

    import random
    
    array =[]

    for i in range(10):

       r=random.randint(1,100)
 
       if r not in array:
                   array.append(r)

    print("Array - ", array)
    print("Array Length - ", len(array))
        
    # Function call
    insertion_sort(array)

    print("Sorted Array - ", array)

