import time
import sys

#This is implemented so python will do recursion until the end of the sorted file for normal quicksort
sys.setrecursionlimit(2000)

def quickSort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quickSort(array, left, q-1)
        quickSort(array, q+1, right)

def quickSortMedian3(array, left, right):
    if left < right:
        n = right - left + 1
        m = median3(array, left, left + n//2, right)
        #exchange A[m] with A[r]
        temp = array[m]
        array[m] = array[right]
        array[right] = temp
        q = partition(array, left, right)
        quickSortMedian3(array, left, q-1)
        quickSortMedian3(array, q+1, right)

def partition(array, left, right):
    x = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= x:
            i = i + 1
            #exchange A[i] with A[j]
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
    #exchange A[i + 1] with A[r]        
    temp = array[right]
    array[right] = array[i + 1]
    array[i + 1] = temp
    return i + 1

def median3(array, left, middle, right):
    #checks if middle is more than left but less than right or more than right but less than left, therefore median
    if array[left] < array[middle] and array[middle] < array[right] or array[right] < array[middle] and array[middle] < array[left]:
        return middle
    #checks if right is more than middle but less than left or more than left but less than middle, therefore median
    elif array[middle] < array[right] and array[right] < array[left] or array[left] < array[right] and array[right] < array[middle]:
        return right
    else:
        return left
    
def selectionSort(array):
    for i in range(len(array)):
        smallsub = i
        for j in range(i+1, len(array)):
            if array[j] < array[smallsub]:
                smallsub = j
        temp = array[i]
        array[i] = array[smallsub]
        array[smallsub] = temp

#copy and pasted the file reader I made for the other labs
def fileReader(filename):
    file = open(filename, "r")
    arraystring = file.read().split(" ")
    stringint = []
    #accounts for weird space at beginning and end of some of the given txt files
    if arraystring[0] == '':
        arraystring.pop(0)
    if arraystring[len(arraystring) - 1] == '':
        arraystring.pop(len(arraystring) - 1)
    #converts the array into integers   
    for x in arraystring:
        stringint.append(int(x))
    file.close()
    return stringint

#Below are the variable names for all of the txt files
file16 = fileReader("input_16.txt")
file32 = fileReader("input_32.txt")
file64 = fileReader("input_64.txt")
file128 = fileReader("input_128.txt")
file256 = fileReader("input_256.txt")
file512 = fileReader("input_512.txt")
file1024 = fileReader("input_1024.txt")
file2048 = fileReader("input_2048.txt")
file4096 = fileReader("input_4096.txt")
file8192 = fileReader("input_8192.txt")
fileRandom = fileReader("input_Random.txt")
fileSorted = fileReader("input_Sorted.txt")
fileReversedSorted = fileReader("input_ReversedSorted.txt")

#Please change this variable to try different file sizes and sorting types i.e., file32, file512, fileSorted
#                 V
currenttest = file8192


#Creating a new array of the same value as currenttest so that changing one will not effect the other
#Otherwise calling currenttest for basic quicksort then median quicksort will have median sorting an already sorted array
#This is done for the median of 3 quicksort
currenttestm = []
for k in range(len(currenttest)):
    currenttestm.append(currenttest[k])
#Same as above but for the insertion sort run
currenttesti = []
for k in range(len(currenttest)):
    currenttesti.append(currenttest[k])

#This is the basic quicksort run
startbasicquick = time.time_ns()
quickSort(currenttest, 0, len(currenttest) - 1)
endbasicquick = time.time_ns()
print("The basic quicksort took", endbasicquick - startbasicquick, "nanoseconds to complete")

#This is the median of 3 quicksort run
startmquick = time.time_ns()
quickSortMedian3(currenttestm, 0, len(currenttestm) - 1)
endmquick = time.time_ns()
print("The median quicksort took", endmquick - startmquick, "nanoseconds to complete")

#This is the insertion sort run
starti = time.time_ns()
selectionSort(currenttesti)
endi = time.time_ns()
print("The selection sort took", endi - starti, "nanoseconds to complete") 

#To test any of the sorted arrays, uncomment the lines below
#print(currenttest)
#print(currenttestm)
#print(currenttesti)