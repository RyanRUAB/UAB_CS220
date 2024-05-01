import time

def insertionSort(array):
    for j in range(0, len(array)):
        current = array[j]
        i = j - 1
        while i >= 0 and array[i] > current:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = current

#file reader function so I wouldn't have to manually import them all
def fileReader(filename):
    file = open(filename, "r")
    arraystring = file.read().split(",")
    stringint = []
    #converts the array into integers   
    for x in arraystring:
        stringint.append(int(x))
    file.close()
    return stringint

#I wrote these as variables outside the main sorting function to not interfere with time
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
#sortedfile is a test file that is 100000 integers long but is already sorted; I wanted to see
#how long it took the code to run against an already sorted list.
#sortedfile = fileReader("sortfile.txt")

start = time.time_ns()
insertionSort(file1000)
print("This took", time.time_ns() - start, "nanoseconds to complete")

