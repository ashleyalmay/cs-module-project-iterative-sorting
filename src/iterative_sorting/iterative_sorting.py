# TO-DO: Complete the selection_sort() function below big O - O(n2)
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc (lines of code))
        # Your code here
        for loop in range(cur_index,len(arr)):
            if arr[loop] < arr[smallest_index]:
                smallest_index = loop

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below big O - O(n2)
def bubble_sort(arr):
    # Your code here
    bub = True
    while bub:
        bub = 0
        for index, item in enumerate(arr):
            if index + 1 < len(arr):
                if arr[index + 1] < item:
                    arr[index], arr[index + 1] = arr[index + 1], arr[index]
                    bub += 1

    return arr
bubble_sort([3,56,7,2,7])
#as long everything is true it will run
#true is = 0
#index, the item will go 1 by 1 in the array
#if the index + 1 is less then the length in the array 
#if the array postion is the index +1  is less then the item
#then if the arrays index, and arrays index + 1 same as arrays index + 1, arrays index
# 0 += 1
#then return the arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
