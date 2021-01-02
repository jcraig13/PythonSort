import random
import time
import sys


# Function to generate random numbers in the given [start, end] range
# and save them in a list. The list is returned
def RandList(start, end, len):
    res = []  # an empty list

    for j in range(len):
        res.append(random.randint(start, end))

    return res


def swap(x, y):
    tmp = x
    x = y
    y = tmp


# return the index of smallest element in list
def FindMinimum(l):
    listlen = len(l)

    ## minV is the minimum value so far
    ## in the beginning, first value is the smallest ...
    minV = l[0]
    minI = 0

    for i in range(1, listlen):  ## i=1, 2, ... listlen-1
        if l[i] < minV:
            minV = l[i]
            minI = i

        ## loop invariant
        ## minV = min (l[left...i]), i.e., min. value seen so far
        ## minV = l[minI]

    return minI


# return the index of smallest element in l[left...right]
def FindMinimum(l, left, right):
    ## minV is the minimum value so far
    ## in the beginning, first value is the smallest ...
    minV = l[left]
    minI = left

    for i in range(left, right + 1):  ## i=left, left+1, ... right
        if l[i] < minV:
            minV = l[i]
            minI = i

        ## loop invariant
        ## minV = min (l[left...i]), i.e., min. value seen so far
        ## minV = l[minI]

    return minI


def SelectionSort(l):
    listlen = len(l)

    for i in range(listlen):  ## i=0, 1, 2, ..., listlen-1
        # fine index of smallest element in l[i...listlen-1]
        minIndex = FindMinimum(l, i, listlen - 1)

        # swap if needed
        # print (minIndex, l[minIndex])

        if minIndex != i:
            # the following does not work!
            # swap (l[i], l[minIndex])
            l[i], l[minIndex] = l[minIndex], l[i]


## sort l[left...right] into ascending order
def RecSelectionSort(l, left, right):
    if (left == right):
        return;

    ## find smallest element's index
    minIndex = FindMinimum(l, left, right)

    ## swap it to the front
    if minIndex != left:
        l[minIndex], l[left] = l[left], l[minIndex]

    # Recursively sort the rest of the list
    RecSelectionSort(l, left + 1, right)


def BubbleSort(l):
    listlen = len(l)

    for j in range(listlen):  ## j=0,1, ... listlen-1

        ## compare adjacent elements, swap them if they are
        ## in wrong order
        for i in range(listlen - 1):  ## i=0, 1, listlen-2
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                ##swap (l[i],l[i+1])


def RecBubbleSort(l, left, right):
    if left == right:
        return

    for i in range(left, right):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]

    RecBubbleSort(l, left, right - 1)

def MergeSort(l):       #Merge Sort using a queue
    if len(l) > 1:
        #find midpoint of list
        mid = len(l) // 2
        #assign left and right sides to divide and conquer
        left = l[:mid]
        right = l[mid:]
        left = MergeSort(left)
        right = MergeSort(right)

        l = []

        #while q contains more the one element...
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                l.append(left[0])
                left.pop(0)
            else:
                l.append(right[0])
                right.pop(0)

        #append the values
        for i in left:
            l.append(i)
        for i in right:
            l.append(i)
    #return the list of sorted values
    return l


def IsSorted(l):
    listlen = len(l)
    for i in range(listlen - 1):  ## i=0,1, ... listlen-2
        if l[i] > l[i + 1]:
            # print(l[i],l[i+1])
            return False

    return True


## testing bubble sort, by visual checking output
a = [20, 3, 4, 6, 1]
RecBubbleSort(a, 0, len(a) - 1)
if IsSorted(a) == False:
    print('bubblesort not working')
print(a)

## Testing selection sort using IsSorted() to verify
## if list is sorted or not
cl = ['a', 'z', 'd', 'g', 'm']
print(cl)
RecSelectionSort(cl, 0, len(cl) - 1)
if IsSorted(cl) == False:
    print('not working')
print(cl)

## test merge sort
b = [3, 4, 19, 10, 44]
print(b)
b = MergeSort(b)
print(b)

print (sys.getrecursionlimit())
sys.setrecursionlimit(3000)

for i in range(10, 2000, 20):  ## i=10,30,50,70, ... 1990OB
    copyl = RandList(1, 10000, i)

    # print (i, 'elapsed:', end_time-start_time)	#print (l)

    l = copyl
    start_time = time.time()
    RecBubbleSort(l, 0, len(l) - 1)
    end_time = time.time()
    recursive_bubble_time = end_time - start_time

    l = copyl
    start_time = time.time()
    BubbleSort(l)
    end_time = time.time()
    bubble_time = end_time - start_time

    l = copyl
    start_time = time.time()
    SelectionSort(l)
    end_time = time.time()
    selection_time = end_time - start_time

    l = copyl
    start_time = time.time()
    RecSelectionSort(l, 0, len(l) - 1)
    end_time = time.time()
    recursive_selection_time = end_time - start_time

    l = copyl
    start_time = time.time()
    MergeSort(l)
    end_time = time.time()
    merge_time = end_time - start_time

    print (i, bubble_time, recursive_bubble_time, selection_time, recursive_selection_time, merge_time)


