def linear_search(arr, target):
    # Your code here big O - O(n)
    for i in range(len(arr)):
        #go thur the arr how ever long it is and print it out
        print(i)
        if (arr[i] == target):
            #if it value is the same as the target then return it
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search big O - O(log(n))
def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr)
    while left < right: 
        x = left + (right - left) //2
        # x = low + (high - low) divied by 2 and return the highest integer
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
#think of the tree and leaves
# when left is less then right the value is x in the array (pointing to the spot)
# x = low + (high - low) divied by 2 and return the highest integer
#