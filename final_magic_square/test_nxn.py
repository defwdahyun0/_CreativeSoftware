import sys
import math

# 초기화
result1 = False
result2 = False

file = open("magic3_output.txt","r") # magic_output.txt 파일을 읽기 모드(r)로 열기 4x4마방진을 읽었습니다.
sum1 = sum2 = sum3 = sum4 = sum5 = sum6 = sum7 = sum8 = p1 = p2 = p3 = p4 = 0
sumnumList = []

try:  
    line = None    # 변수 line을 None으로 초기화
    while line != '':

        line = file.readline()
        inlst = line.strip('\n ')#print(line.strip('\n')) # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
        inList = inlst.split(' ')
        numList = list(map(int, inList))
        ns = len(numList)
        nss = int(math.sqrt(ns))

        sumnumList.append(numList)

        if nss % 2 != 0: #홀수 마방진
            sum1 = sum2 = sum3 = sum4 = 0
            for i in range(int(nss)): 
                for j in range(int(nss)):
                    sum1 = sum1 + numList[j+nss*i] #가로 한 줄의 합
                    sum2 = sum2 + numList[(nss)*j+i] #세로 한 줄의 합
                sum3 = sum3 + numList[(nss+1)*i] #오른쪽 대각선의 합
                sum4 = sum4 + numList[(nss-1)*(i+1)] #왼쪽 대각선의 합
            #print(sum1//nss,sum2//nss,sum3,sum4)
            if (sum1//nss == sum2//nss == sum3 == sum4):
                result1 = True
            print('{} - {}'.format(inlst,result1)) #홀수 마방진의 성립 여부
        else: #짝수 마방진
            sum5 = sum6 = sum7 = sum8 = p1 = p2 = p3 = p4 = 0
            for i in range(int(nss)):
                for j in range(int(nss)):
                    sum5 = sum5 + numList[j+nss*i] #가로 한줄의 합
                    sum6 = sum6 + numList[(nss)*j+i] #세로 한줄의 합
                sum7 = sum7 + numList[(nss+1)*i] #오른쪽 대각선의 합
                sum8 = sum8 + numList[(nss-1)*(i+1)] #왼쪽 대각선의 합
            # 4분할 partition의 합
            for i in range(int(nss//2)):
                for j in range(int(nss//2)):
                    p1 = p1 + numList[i + nss*j]
            for i in range(int(nss//2)):
                for j in range(int(nss//2)):
                    p2 = p2 + numList[nss//2 +i + nss*j]
            for i in range(int(nss//2)):
                for j in range(int(nss//2)):
                    p3 = p3 + numList[i + nss*(j+nss//2)]
            for i in range(int(nss//2)):
                for j in range(int(nss//2)):
                    p4 = p4 + numList[i+nss//2 + nss*(j+nss//2)]
            #print(sum5//nss,sum6//nss,sum7,sum8,p1,p2,p3,p4)
            if (sum5//nss == sum6//nss == sum7 == sum8 == p1 == p2 == p3 == p4):
                result2 = True
            print('{} - {}'.format(inlst,result2)) #짝수 마방진의 성립 여부
except ValueError:
    pass
except EOFError:
    print("EOFError가 발생했습니다.")
file.close()

#print(sumnumList)
#print(len(sumnumList))

unique = []
for s in sumnumList:
    if s not in unique:
        unique.append(s)
#print(len(unique))

if len(sumnumList) == len(unique):
    print("중복이 없습니다.")
