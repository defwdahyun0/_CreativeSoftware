import sys
filep = open("output.txt", "w") #"rw" cannot be use
a = 100
b = "String_B"
print("----------Sep----------")
print("Deafult   - ", a, b)
print("Sep=$$$   - ", a, b, sep='$$$')
print("Sep=\_n   - ", a, b, sep='\n') ## 앞에 \n을 그냥쓰면 거기 줄바꿈 
print("Sep=''    - ", a, b, sep='')
print("----------End----------")
print("End=''    - ", a, b, end='')
print("Next Line", end='')
print("----------End----------")
print("End=''    - ", a, b, end='=====\n')
print("Next Line", end='=====\n')
print("----------End--FILE--------")
print("End=''    - ", a, b, end='=====\n')
print("   sys.stdin - type ", type(sys.stdout))
print("Next Line", end='=====\n', file=filep)
print("Next Line", end='=====\n', file=filep, flsuh=True) # We don't know how to use it
filep.close()
