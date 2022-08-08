
# Read the input
inputFile = open("D:\School\orac\simple addition\sitin.txt", "r")
outputFile = open("D:\School\orac\simple addition\sitout.txt", "w")
 
n = int(inputFile.readline())
b = 1
d = 1

idays = 0 #number of days


# 
#n % 2 != 0 #if it is an odd number
while 2**b * b != n: #while i^bxb does not equal to the value of n
    idays += 1
    if n % 2 != 0: #if it is an odd number
        b += 1 #contines it odd
    else: #if it is an even number
        b += 2 #makes it odd
    print(b)
    
    if 2**b * b == n:
        break #breaks the loop

b = str(b)
d = str(idays)

outputFile.write(f"{b} {d}")
 
# Clean up!
inputFile.close()
outputFile.close()
