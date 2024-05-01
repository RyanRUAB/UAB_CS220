import time

TABLE_SIZE = 100
class HashMap:
#By setting TABLE_SIZE as a global variable it makes it possible to be accessed by other
#functions in the code
    def __init__(self):
        global TABLE_SIZE
        self.size = TABLE_SIZE
        self.hashmap = [None] * TABLE_SIZE
#Because the hash is an array of lists, two types of indexing must be done. 
#One for self.hashmap and one for the i variable which is the key-value pair
    def get(self, key):
        index = key % self.size
        if self.hashmap[index] is not None:
            for i in self.hashmap[index]:
                if i[0] == key:
                    return i[1]
        else:
            return None

    def put(self, key, value):
        index = key % self.size
        pair = [key, value]        
        if self.hashmap[index] is None:
            self.hashmap[index] = list([pair])
        elif self.hashmap[index][0] != pair[0]:
            count = 0
            while count < 100:
                temp = index
                index = (7*index + 1) % self.size
                if self.hashmap[index] is None:
                    self.hashmap[index] = list([pair])
                    break
                elif count == 99 and self.hashmap[index] is not None:
                    self.hashmap[temp] = list([pair])
                    break
                count += 1
        else:
            self.hashmap[index][1] = pair[1]
#This function prints every hash, that isn't empty, on its own line to make it easy to see
    def printhash(self):
        for i in self.hashmap:
            if i is not None:
                print(i)

    def linear_probe(self, key, value):
        index = key % self.size
        pair = [key, value] 
        count = 0
        while count < 200:
            if self.hashmap[index] is not None:
                index += 1
                index = index % self.size
                count += 1
            else:
                self.hashmap[index] = list([pair])
                break

#The quadcount variable is the count that keeps track of quadratic leaps in the function
    def quadratic_probe(self, key, value):
        index = key % self.size
        pair = [key, value]
        quadcount = 1
        temp = index
        count = 0
        while count < 200:
            if self.hashmap[temp] is not None:
                temp = index
                temp += quadcount*quadcount
                temp = temp % self.size
                quadcount += 1
                count += 1
            else:
                self.hashmap[temp] = list([pair])
                break

#A file reader made from the skeleton of my old filereaders, this one is very different
#though as it reads by line rather than the whole file.
def fileReader(filename):
    file = open(filename, "r")
    arraylines = []
    while True:
        line = file.readline()
        if not line:
            break
        linestripped = line.strip() 
        if ",," in line:
            x = linestripped.split(",,", 1)
            try:
                arraylines.append(int(x[0]))
                arraylines.append(x[1])
            except ValueError:
                x = linestripped.split(",", 1)
                arraylines.append(int(x[0]))
                arraylines.append(x[1]) 
        else:
            x = linestripped.split(",", 1)
            arraylines.append(int(x[0]))
            arraylines.append(x[1])   
    file.close()
    return arraylines

#These are just the file variable for the different files to be read
input = fileReader("input.dat")
upc = fileReader("UPC.csv")
upcRandom = fileReader("UPC-random.csv")

#Primary intialization of the hashmap
hash = HashMap()

#I just made this so I could change between files quickly 
def fileReaderPut(filename):
    count = 0
    while count < len(filename):
        hash.put(filename[count], filename[count + 1])
        count += 2

def linearProbingHash(filename):
    count = 0
    while count < len(filename):
        hash.linear_probe(filename[count], filename[count + 1])
        count += 2

def quadraticProbingHash(filename):
    count = 0
    while count < len(filename):
        hash.quadratic_probe(filename[count], filename[count + 1])
        count += 2

#uncomment the funciton you would like to test

#UPC testers
#start = time.time_ns()
#fileReaderPut(upc)
#linearProbingHash(upc)
#quadraticProbingHash(upc)
#end = time.time_ns()
#print("This test took", end - start, "nanoseconds to complete")

#UPC-random testers
start = time.time_ns()
#fileReaderPut(upcRandom)
#linearProbingHash(upcRandom)
quadraticProbingHash(upcRandom)
end = time.time_ns()   
print("This test took", end - start, "nanoseconds to complete")

#input.dat testers
#start = time.time_ns()
#fileReaderPut(input)
#linearProbingHash(input)
#quadraticProbingHash(input)
#end = time.time_ns()
#print("This test took", end - start, "nanoseconds to complete")

#Simple print test functions to show that the hashmap is complete and the get
#function works
#hash.printhash()
#print(hash.get(93))