def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        print(i)
        if (arr[i] == target):
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr)
    while left < right: 
        x = left + (right - left) //2
        value = arr[x]
        if target == value:
            return x
        elif target > value:
            if left == x:
                break
            left = x
        elif target < value:
            right = x 


    return -1  # not found
#left is the lower side right is higher 