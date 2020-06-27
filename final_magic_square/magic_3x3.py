import sys
import itertools as i
import time

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

sumOfList = sum(numList)
if (sumOfList % 3 != 0):
    print("Error : Sum is not times of 3", file=sys.stderr) #마방진을 풀 수 없다.
    exit()
sumOfLine = sumOfList // 3
print(sumOfLine)

num=0
start= time.time()
file = open("magic3_output.txt","w")
match = 0
for a in set(numList):
    L1 = numList.copy()
    L1.remove(a)
    for b in set(L1):
        L2 = L1.copy()
        L2.remove(b)
        c = sumOfLine-a-b
        if (not(c in L2)):
            continue
        else:
            L3 = L2.copy()
            L3.remove(c)
            for d in set(L3):
                L4 = L3.copy()
                L4.remove(d)
                for e in set(L4): 
                    L5 = L4.copy()
                    L5.remove(e)
                    for f in set(L5):
                        if (d+e+f != sumOfLine):
                            continue
                        L6 = L5.copy()
                        L6.remove(f)
                        for g in set(L6):
                            if (a+d+g != sumOfLine):
                                continue
                            if (c+e+g != sumOfLine):
                                continue
                            L7 = L6.copy()
                            L7.remove(g)
                            for h in set(L7):
                                if (b+e+h != sumOfLine):
                                    continue
                                L8 = L7.copy()
                                L8.remove(h)
                                for i in set(L8):
                                    if (g+h+i == c+f+i == a+e+i == sumOfLine): 
                                        print(a,b,c,d,e,f,g,h,i)
                                        fstr = [str(a),str(b),str(c),str(d),str(e),str(f),str(g),str(h),str(i),'\n']
                                        file.write(' '.join(fstr))
                                        match += 1
'''
finallist = set(list(i.permutations(numList, 9)))
for a in finallist:
    if (a[0]+a[1]+a[2] == a[3]+a[4]+a[5] == a[6]+a[7]+a[8] == a[0]+a[3]+a[6] == a[1]+a[4]+a[7] == a[2]+a[5]+a[8] == a[0]+a[4]+a[8] == a[2]+a[4]+a[6] == sumOfLine): 
        print(a)
        num+=1
# 주석처럼 코드를 짤 수도 있다. 수행시간은 길어지지만, 코드의 길이가 짧다는 점에서 이점이 있다.
'''
file.close()
print("Total Match = ", match, file = sys.stderr)
print("Execution Time =", time.time() - start, file = sys.stderr)
print("총 {} 개의 답이 있습니다. 계산시간은 {} 초 입니다. ".format(match,time.time() - start), file = sys.stderr)