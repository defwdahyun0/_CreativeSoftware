import sys
import math

# 초기화
result1 = False
result2 = False

file = open("magic4_output.txt","r") #예시, 4x4 마방진 읽기.
sum1 = sum2 = sum3 = sum4 = sum5 = sum6 = sum7 = sum8 = p1 = p2 = p3 = p4 = 0
sumnumList = []

try:  
    line = None
    while line != '':
        line = file.readline()
        inlst = line.strip('\n ') #파일에서 읽어온 문자열에서 \n 삭제하여 출력
        inList = inlst.split(' ')
        numList = list(map(int, inList))
        ns = len(numList)
        nss = int(math.sqrt(ns))

        sumOfList = sum(numList)
        sumOfLine = sumOfList // nss

        sumnumList.append(numList)

        if nss == 3: #3x3 마방진일 때.
            if (numList[0]+numList[1]+numList[2] == numList[3]+numList[4]+numList[5] == numList[6]+numList[7]+numList[8] == numList[0]+numList[3]+numList[6] == numList[1]+numList[4]+numList[7] == numList[2]+numList[5]+numList[8] == numList[0]+numList[4]+numList[8] == numList[2]+numList[4]+numList[6] == sumOfLine): 
                result1 = True
            print('{} - {}'.format(inlst,result1)) #3x3 마방진의 성립 여부
        elif nss == 4: #4x4 마방진일 때.
            if (numList[0]+numList[1]+numList[2]+numList[3] == numList[4]+numList[5]+numList[6]+numList[7] == numList[8]+numList[9]+numList[10]+numList[11] == numList[12]+numList[13]+numList[14]+numList[15] == numList[0]+numList[4]+numList[8]+numList[12] == numList[1]+numList[5]+numList[9]+numList[13] == numList[2]+numList[6]+numList[10]+numList[14] == numList[3]+numList[7]+numList[11]+numList[15] == numList[0]+numList[5]+numList[10]+numList[15] == numList[3]+numList[6]+numList[9]+numList[12] == numList[0]+numList[1]+numList[4]+numList[5] == numList[2]+numList[3]+numList[6]+numList[7] == numList[8]+numList[9]+numList[12]+numList[13] == numList[10]+numList[11]+numList[14]+numList[15] == sumOfLine): 
                result1 = True
            print('{} - {}'.format(inlst,result1)) #4x4 마방진의 성립 여부
        elif nss % 2 != 0: #홀수 마방진
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
        elif nss % 2 == 0: #짝수 마방진
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
else:
    print("중복이 있습니다.")