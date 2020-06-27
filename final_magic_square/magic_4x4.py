import copy
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
print(numList)
print("stderr :", numList, file = sys.stderr)
print("stdout :", numList, file = sys.stdout)

sumOfList = sum(numList)
if (sumOfList % 4 != 0):
    print("Error : Sum is not times of 4", file=sys.stderr) #마방진을 풀 수 없다.
    exit()
sumOfLine = sumOfList // 4
print("이 마방진에서 한 줄의 합은",sumOfLine,"이다.")

# new_list_remove fucntion을 통해 list의 요소 제거
def new_list_remove(src, a):
  new_list = copy.copy(src)
  new_list.remove(a)
  return new_list

num=0
start= time.time()
file = open("magic4_output.txt","w")
match = 0
for a in set(numList):
    blist = new_list_remove(numList, a)
    for b in set(blist):
        clist = new_list_remove(blist, b)
        for c in set(clist):
            dlist = new_list_remove(clist, c) 
            for d in set(dlist):
                if(a + b + c + d != sumOfLine): # 맨윗줄
                    continue
                elist = new_list_remove(dlist,d)
                for e in set(elist):
                    flist = new_list_remove(elist,e)
                    for f in set(flist):
                        if(a + b + e + f != sumOfLine):
                            continue
                        glist = new_list_remove(flist,f)
                        for g in set(glist):
                            hlist = new_list_remove(glist,g)
                            for h in set(hlist):
                                if (c + d + g + h != sumOfLine or e + f + g + h != sumOfLine):
                                    continue
                            ilist = new_list_remove(hlist,h)
                            for i in set(ilist):
                                jlist = new_list_remove(ilist,i)
                                for j in set(jlist):
                                    klist = new_list_remove(jlist,j)
                                    for k in set(klist):
                                        llist = new_list_remove(klist,k)
                                        for l in set(llist):
                                            if (i + j + k + l != sumOfLine):
                                                continue
                                            mlist = new_list_remove(llist,l)
                                            for m in set(mlist):
                                                if (a + e + i + m != sumOfLine or d + g+ j + m != sumOfLine):
                                                    continue
                                                nlist = new_list_remove(mlist,m)
                                                for n in set(nlist):
                                                    if (b+f+j+n != sumOfLine or i + j + m +n != sumOfLine):
                                                        continue
                                                    olist = new_list_remove(nlist,n)
                                                    for o in set(olist):
                                                        if (c+g+k+o != sumOfLine):
                                                            continue
                                                        plist = new_list_remove(olist,o)
                                                        for p in set(plist):
                                                            if ((m + n + o + p) != sumOfLine or (d + h + l + p) != sumOfLine):
                                                                continue
                                                            if ((a + f + k + p) != sumOfLine or (k + l + o + p) != sumOfLine):
                                                                continue 
                                                            print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
                                                            fstr = [str(a),str(b),str(c),str(d),str(e),str(f),str(g),str(h),str(i),str(j),str(k),str(l),str(m),str(n),str(o),str(p),'\n']
                                                            file.write(' '.join(fstr))
                                                            match += 1
file.close()
print("Total Match = ", match, file = sys.stderr)
print("Execution Time =", time.time() - start, file = sys.stderr)
print("총 {} 개의 답이 있습니다. 계산시간은 {} 초 입니다. ".format(match,time.time() - start), file = sys.stderr)

