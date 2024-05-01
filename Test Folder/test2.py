from queue import PriorityQueue

mytuple = [("Apples", "banana", "cherries"), ("Alpha", "Beta", "Gamma")]

print(mytuple[0][1])

class Vertex:
    def __init__(self, name):
        self.name = name
    

mydict = {"a":"bear", "b":"dog"}
if "x" not in mydict.keys():
    mydict["x"] = "raven"

print(mydict.values())

for i in mydict.items():
    print(i)

queue = PriorityQueue()
queue.put((10, "a"))
queue.put((4, "b"))
queue.put((3,"c"))


while queue is not []:
    print(queue.get())
    print(queue.queue)
