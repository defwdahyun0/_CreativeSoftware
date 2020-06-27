import sys
import itertools as ii
import time
import math

inList = input()
print("stderr :", inList, file = sys.stderr)
print("stdout :", inList, file = sys.stdout)
inList = inList.split(" ")
print("stderr :", inList, file = sys.stderr)
print("stdout :", inList, file = sys.stdout)
numList=[] 
for a in inList:
    numList.append(int(a))
print("stderr :", numList, file = sys.stderr)
print("stdout :", numList, file = sys.stdout)
print(numList)

ns = len(numList) # nxn 마방진의 길이
nss = int(math.sqrt(ns)) # 그 때의 n

sumOfList = sum(numList)
if (sumOfList % nss != 0):
    print("Error : Sum is not times of {}".format(nss), file=sys.stderr) #마방진을 풀 수 없다.
    exit()
sumOfLine = sumOfList // nss
print("이 마방진에서 한 줄의 합은",sumOfLine,"이다.")

horizontal  = []
vertical = []
match=0
start = time.time()

finallist = set(list(ii.permutations(numList, ns)))
if nss % 2 != 0: #홀수 마방진
    for a in finallist:
        sum1 = sum2 = sum3 = sum4 = 0
        for i in range(int(nss)):
            for j in range(int(nss)):
                sum1 = sum1 + a[j+nss*i] #가로 한 줄의 합
                sum2 = sum2 + a[(nss)*j+i] #세로 한 줄의 합
            sum3 = sum3 + a[(nss+1)*i] #오른쪽 대각선의 합
            sum4 = sum4 + a[(nss-1)*(i+1)] #왼쪽 대각선의 합
        if (sum1//nss == sum2//nss == sum3 == sum4 == sumOfLine):
            print(a)
            match+=1
elif nss % 2 == 0: #짝수 마방진
    for a in finallist: 
        sum5 = sum6 = sum7 = sum8 = p1 = p2 = p3 = p4 = 0
        for i in range(int(nss)):
            for j in range(int(nss)):
                sum5 = sum5 + a[j+nss*i] #가로 한줄의 합
                sum6 = sum6 + a[(nss)*j+i] #세로 한줄의 합
            sum7 = sum7 + a[(nss+1)*i] #오른쪽 대각선의 합
            sum8 = sum8 + a[(nss-1)*(i+1)] #왼쪽 대각선의 합
        # 4분할 partition의 합
        for i in range(int(nss//2)):
            for j in range(int(nss//2)):
                p1 = p1 + a[i + nss*j]
        for i in range(int(nss//2)):
            for j in range(int(nss//2)):
                p2 = p2 + a[nss//2 +i + nss*j]
        for i in range(int(nss//2)):
            for j in range(int(nss//2)):
                p3 = p3 + a[i + nss*(j+nss//2)]
        for i in range(int(nss//2)):
            for j in range(int(nss//2)):
                p4 = p4 + a[i+nss//2 + nss*(j+nss//2)]
        if (sum5//nss == sum6//nss == sum7 == sum8 == p1 == p2 == p3 == p4):
            print(a)
            match+=1
print("Total Match = ", match, file = sys.stderr)
print("Execution Time =", time.time() - start, file = sys.stderr)
print("총 {} 개의 답이 있습니다. 계산시간은 {} 초 입니다. ".format(match,time.time() - start), file = sys.stderr)