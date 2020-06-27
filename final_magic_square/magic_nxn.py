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
if (sumOfList % ns != 0):
    print("Error : Sum is not times of {}".format(nss), file=sys.stderr) #마방진을 풀 수 없다.
    exit()
sumOfLine = sumOfList // nss
print(sumOfLine)

match=0
start = time.time()
finallist = set(list(ii.permutations(numList, 9)))
for a in finallist:
    sum1 = sum2 = sum3 = sum4 = 0

    for k in range(int(nss)):
        for i in range(int(nss)): #한줄씩의 합, nss번 반복할 것이다.
            sum1 = sum1 + a[i+nss*k] #가로 한 줄의 합 #등차수열 
            sum2 = sum2 + a[k+(nss)*i] #세로 한 줄의 합 #등비수열 
        sum3 = sum3 + a[(nss+1)*i] #오른쪽 대각선의 합
        sum4 = sum4 + a[(nss-1)*(i+1)] #왼쪽 대각선의 합

        print(sum1,sum2,sum3,sum4)
        if (sum1//nss == sum2//nss == sum3 == sum4 == sumOfLine):
            print(a)
            match+=1
print("Total Match = ", match, file = sys.stderr)
print("Execution Time =", time.time() - start, file = sys.stderr)
print("총 {} 개의 답이 있습니다. 계산시간은 {} 초 입니다. ".format(match,time.time() - start), file = sys.stderr)