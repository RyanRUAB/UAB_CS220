#I Ryan Roberts worked alone

import socket
import random
import time

socket.setdefaulttimeout(120)
localhost = ''
#Input the local IP address of the target computer, this applies if connecting to self
#This number can be found using ipconfig(windows) or ifconfig(mac/linux)
server = "192.168.56.1" #Currently set to my local IP

#Step 2
print("Creating a socket to connect to ROBOT at port 3310")
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((server, 3310))
print("Connected")
print("\nSending Blazer ID to Robot")
#My Blazer ID here
blazerid = input("Type in your Blazer ID: ")
s1.send(blazerid.encode())
#Step 3
print("Receiving Robot response")
reply = s1.recv(100)
reply = int(reply)
print("Received")

print("\nCreating TCP socket at port %d" %reply)
listensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listensocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listensocket.bind((localhost, reply))
listensocket.listen()
print("Done")

s2, address = listensocket.accept()
robotIP = address[0]
print("\nRobot from %s at port %d connected" %(robotIP, address[1]))

listensocket.close()
#Step 4
reply2 = s2.recv(100)
reply2decode = reply2.decode()
reply2list = reply2decode.split(",")
robotport = int(reply2list[0])
studentport = int(reply2list[1])

print("\nPorts received: Robot<%d> and Student<%d>" %(robotport, studentport))

num = random.randint(6,9)

s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s3.bind((localhost, studentport))

#The message was  originally sending before the port was opened so it needed to sleep
time.sleep(1)

print("\nSending random number %d to Robot" %num)
s3.sendto(str(num).encode(), (robotIP, robotport))

x, robotaddress = s3.recvfrom(1024)
x = x.decode()
print("Receiving Robot response %s" %x)
#Time given for the other four messages to finish being delivered
time.sleep(5)
#Step 5
#print("\nSending Robot message back to it 5 times")
for i in range(0,5):
    s3.sendto(x.encode(),(robotIP,robotport))
    print("Packet", i + 1, "sent")
    time.sleep(1)
print("Done")

s1.close()
s2.close()
s3.close()
exit()