import time
#I needed to create the node class in order to use the .left and .right
class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
#I intialize the node class here so that the .left and .right can be made use of
def treeInsert(T, z):
    n = node(z)
    y = None
    x = T
    while x is not None:
        y = x
        if z < x.key:
            x = x.left
        else:
            x = x.right
    #n.p = y / This never did anything so it is commented out
    if y is None:
        y = n
    elif z < y.key:
        y.left = n
    else:
        y.right = n
    return n

def inorderTreeWalk(x):
    if x is not None:
        inorderTreeWalk(x.left)
        print(x.key)
        inorderTreeWalk(x.right)

def treeSearch(x, k):
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x.key

#The previous filereader I made during lab 6 the only difference being I only want the
#numbers this time
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
                #arraylines.append(x[1])
            except ValueError:
                x = linestripped.split(",", 1)
                arraylines.append(int(x[0]))
                #arraylines.append(x[1]) 
        else:
            x = linestripped.split(",", 1)
            arraylines.append(int(x[0]))
            #arraylines.append(x[1])   
    file.close()
    return arraylines

input = fileReader("input.dat")
upc = fileReader("UPC.csv")
upcRandom = fileReader("UPC-random.csv")

#Quick test tree to show that the inorderTreeWalk works and that the tree builds correctly
testtree = None
testtree = treeInsert(testtree, 100)
treeInsert(testtree, 23)
treeInsert(testtree, 57)
treeInsert(testtree, 38)
treeInsert(testtree, 79)
treeInsert(testtree, 82)
treeInsert(testtree, 4)
treeInsert(testtree, 42)

inorderTreeWalk(testtree)

#Building the tree using the upc file
tree = None
#Assigning the root node here, I'm assigning it in the middle so it is more balanced
tree = treeInsert(tree, upcRandom[0])
for i in range(1, len(upcRandom)):
    treeInsert(tree, upcRandom[i])

#If you would like to see the fully created tree from the upc random, uncomment the below line
#inorderTreeWalk(tree)

start = time.time_ns()
for i in range(len(input)):
    print(treeSearch(tree, input[i]))
end = time.time_ns()


print("To find all keys in the upc tree it took",  end - start,  "nanoseconds to complete")