import time

#setting heapsize as a global variable allows it to be controlled by all functions
heapsize = 0

def heapSort(array):
    buildMaxHeap(array)
    #using range's "step" capabilities to negatively step through the range: the -1
    #the negative step is exclusive though so the stop has to be 1 lower to account for the exclusion
    for i in range(len(array) - 1, 0, -1):
        #I realized just setting one equal to the other wasn't working so I had to create temp variables
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        global heapsize
        heapsize = heapsize - 1
        maxHeapify(array, 0)

def buildMaxHeap(array):
    global heapsize
    #heapsize has to be -1 of the array length due to indexing at 0
    heapsize = len(array) - 1
    for i in range(len(array) // 2, -1, -1):
        maxHeapify(array, i)

def maxHeapify(array, i):
    #the left child will always be 2 times the parent index
    l = 2*i
    #the right child will always be 2 times the parent index plus 1
    r = (2*i) + 1
    global heapsize
    if l <= heapsize and array[l] >= array[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize and array[r] >= array[largest]:
        largest = r
    if largest != i:
        #same issue as in heapSort where I needed temp variables for the swap
        temp = array[i]
        array[i] = array[largest]
        array[largest] = temp
        maxHeapify(array, largest)

#copy and pasted the file reader I made for the other labs
def fileReader(filename):
    file = open(filename, "r")
    arraystring = file.read().split(",")
    stringint = []
    #converts the array into integers   
    for x in arraystring:
        stringint.append(int(x))
    file.close()
    return stringint

#as well as the variables for easy access, except for 1000000
file1000 = fileReader("1000.txt")
file2500 = fileReader("2500.txt")
file5000 = fileReader("5000.txt")
file10000 = fileReader("10000.txt")
file25000 = fileReader("25000.txt")
file50000 = fileReader("50000.txt")
file100000 = fileReader("100000.txt")
file250000 = fileReader("250000.txt")
file500000 = fileReader("500000.txt")

#in earlier labs I had a variable that controlled which file was being sorted
#for this one I just have all of them 
start1000 = time.time_ns()
heapSort(file1000)
end1000 = time.time_ns()
print("The 1000 item heap sort took", end1000 - start1000, "nanoseconds to complete")

start2500 = time.time_ns()
heapSort(file2500)
end2500 = time.time_ns()
print("The 2500 item heap sort took", end2500 - start2500, "nanoseconds to complete")

start5000 = time.time_ns()
heapSort(file5000)
end5000 = time.time_ns()
print("The 5000 item heap sort took", end5000 - start5000, "nanoseconds to complete")

start10000 = time.time_ns()
heapSort(file10000)
end10000 = time.time_ns()
print("The 10000 item heap sort took", end10000 - start10000, "nanoseconds to complete")

start25000 = time.time_ns()
heapSort(file25000)
end25000 = time.time_ns()
print("The 25000 item heap sort took", end25000 - start25000, "nanoseconds to complete")

start50000 = time.time_ns()
heapSort(file50000)
end50000 = time.time_ns()
print("The 50000 item heap sort took", end50000 - start50000, "nanoseconds to complete")

start100000 = time.time_ns()
heapSort(file100000)
end100000 = time.time_ns()
print("The 100000 item heap sort took", end100000 - start100000, "nanoseconds to complete")

start250000 = time.time_ns()
heapSort(file250000)
end250000 = time.time_ns()
print("The 250000 item heap sort took", end250000 - start250000, "nanoseconds to complete")

start500000 = time.time_ns()
heapSort(file500000)
end500000 = time.time_ns()
print("The 500000 item heap sort took", end500000 - start500000, "nanoseconds to complete")

#If you would like to check that the files are being sorted, uncomment the print line below
#print(file1000)