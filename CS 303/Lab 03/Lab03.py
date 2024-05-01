import time
import random

def randomArray(length):
    rarray = []
    for k in range(length):
        rarray.append(random.randrange(0, length))
    return rarray



#I wanted my variables to be left, middle, and right for readability as these are the 
#index positions of the array at any given time
def mergeSort(array, temp, left, right):
    if left < right:
        #dividing in python with only / converts to float so it must be // to do integer division
        middle = (left + right) // 2
        mergeSort(array, temp, left, middle)
        mergeSort(array, temp, middle+1, right)
        merge(array, temp, left, middle, right)

def merge(array, temp, left, middle, right):
    i = left
    j = middle + 1
    #right has to be +1 because range in python is exclusive
    #meaning if left is 0 and right was 1, it would be a range of 0 not 0, 1
    for k in range(left, right+1):
        temp[k] = array[k]
    for k in range(left, right+1):
        if i > middle:
            array[k] = temp[j]
            j = j + 1
        elif j > right:
            array[k] = temp[i]
            i = i + 1
        elif temp[j] < temp[i]:
            array[k] = temp[j]
            j = j + 1
        else:
            array[k] = temp[i]
            i = i + 1

#insertion sort copied and pasted from lab 2
def insertionSort(array):
    for j in range(0, len(array)):
        current = array[j]
        i = j - 1
        while i >= 0 and array[i] > current:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = current



#copy and pasted the file reader I made for lab 02 here
def fileReader(filename):
    file = open(filename, "r")
    arraystring = file.read().split(",")
    stringint = []
    #converts the array into integers   
    for x in arraystring:
        stringint.append(int(x))
    file.close()
    return stringint

#as well as the variables for easy access
file1000 = fileReader("1000.txt")
file2500 = fileReader("2500.txt")
file5000 = fileReader("5000.txt")
file10000 = fileReader("10000.txt")
file25000 = fileReader("25000.txt")
file50000 = fileReader("50000.txt")
file100000 = fileReader("100000.txt")
file250000 = fileReader("250000.txt")
file500000 = fileReader("500000.txt")
file1000000 = fileReader("1000000.txt")

#change the number of the randomArray function to change the array size of filerandom
filerandom = randomArray(150)


#change this variable to test different sizes in the main function
testfile = filerandom

#doing this to create a new array of the same value so that changing one will not affect the other
testfilei = []
for k in range(len(testfile)):
    testfilei.append(testfile[k])

#allocating the temp arrays ahead of time
temptest = [0] * len(testfile)

#comment out the if-else statement if you would like to see both at the same time
if len(testfile) > 150:
    #Merge Sort
    start = time.time_ns()
    mergeSort(testfile, temptest, 0, len(testfile) - 1)
    end = time.time_ns()
    print("This merge sort took", end - start, "nanoseconds to complete")

else:
    #Insertion Sort
    starti = time.time_ns()
    insertionSort(testfilei)
    endi = time.time_ns()
    print("This insertion sort took ", endi - starti, "nanoseconds to complete")


#a print function to check that the arrays are being sorted, just uncomment it
#print(testfile)
#print(testfilei)