import sys
import math

file = open("magic3_output.txt","r") #예시, 4x4 마방진 읽기.
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
        nsq = math.sqrt(ns) #nsquestion. nxn인지 체크하기 위해 만들었다.
        nss = int(math.sqrt(ns))

        sumOfList = sum(numList)
        sumOfLine = sumOfList // nss

        sumnumList.append(numList)

        # 초기화
        result1 = False
        result2 = False

        hoochoo = 0 # 마방진 확인을 위한 변수, 우리집 고양이들의 이름. 후추와 나리.
        nari = 0
        '''
        if nss == 3: #3x3 마방진일 때.
            if (numList[0]+numList[1]+numList[2] == numList[3]+numList[4]+numList[5] == numList[6]+numList[7]+numList[8] == numList[0]+numList[3]+numList[6] == numList[1]+numList[4]+numList[7] == numList[2]+numList[5]+numList[8] == numList[0]+numList[4]+numList[8] == numList[2]+numList[4]+numList[6] == sumOfLine): 
                result1 = True
            print('{} - {}'.format(inlst,result1)) #3x3 마방진의 성립 여부
        elif nss == 4: #4x4 마방진일 때.
            if (numList[0]+numList[1]+numList[2]+numList[3] == numList[4]+numList[5]+numList[6]+numList[7] == numList[8]+numList[9]+numList[10]+numList[11] == numList[12]+numList[13]+numList[14]+numList[15] == numList[0]+numList[4]+numList[8]+numList[12] == numList[1]+numList[5]+numList[9]+numList[13] == numList[2]+numList[6]+numList[10]+numList[14] == numList[3]+numList[7]+numList[11]+numList[15] == numList[0]+numList[5]+numList[10]+numList[15] == numList[3]+numList[6]+numList[9]+numList[12] == numList[0]+numList[1]+numList[4]+numList[5] == numList[2]+numList[3]+numList[6]+numList[7] == numList[8]+numList[9]+numList[12]+numList[13] == numList[10]+numList[11]+numList[14]+numList[15] == sumOfLine): 
                result2 = True
            print('{} - {}'.format(inlst,result1)) #4x4 마방진의 성립 여부
        '''
        if nss % 2 != 0: #홀수 마방진
            sum1 = sum2 = sum3 = sum4 = 0
            for i in range(int(nss)):
                for j in range(int(nss)):
                    sum1 = sum1 + numList[j+nss*i] #가로 한 줄의 합
                if sum1 == sumOfLine:
                    hoochoo += 1
                sum1 = 0    
                for j in range(int(nss)):
                    sum2 = sum2 + numList[(nss)*j+i] #세로 한 줄의 합
                if sum2 == sumOfLine:
                    nari += 1
                sum2 = 0    
                sum3 = sum3 + numList[(nss+1)*i] #오른쪽 대각선의 합
                sum4 = sum4 + numList[(nss-1)*(i+1)] #왼쪽 대각선의 합
            if (nari == hoochoo == nss and sum3 == sum4 == sumOfLine):
                result1 = True
            print('{} - {}'.format(inlst,result1)) #홀수 마방진의 성립 여부
        elif nss % 2 == 0: #짝수 마방진
            sum5 = sum6 = sum7 = sum8 = p1 = p2 = p3 = p4 = 0
            for i in range(int(nss)):
                for j in range(int(nss)):
                    sum5 = sum5 + numList[j+nss*i] #가로 한 줄의 합
                if sum5 == sumOfLine:
                    hoochoo += 1
                sum5 = 0    
                for j in range(int(nss)):
                    sum6 = sum6 + numList[(nss)*j+i] #세로 한 줄의 합
                if sum6 == sumOfLine:
                    nari += 1
                sum6 = 0    
                sum7 = sum7 + numList[(nss+1)*i] #오른쪽 대각선의 합
                sum8 = sum8 + numList[(nss-1)*(i+1)] #왼쪽 대각선의 합
            # 4분할 partition의 합
            for i in range(int(nss//2)):
                for j in range(int(nss//2)):
                    p1 = p1 + numList[i + nss*j]
                    p2 = p2 + numList[nss//2 +i+ nss*j]
                    p3 = p3 + numList[i + nss*(j+nss//2)]
                    p4 = p4 + numList[i+nss//2 + nss*(j+nss//2)]
            if (nari == hoochoo == nss and  p1 == p2 == p3 == p4 == sum7 == sum8 == sumOfLine):
                result2 = True
            print('{} - {}'.format(inlst,result2)) #짝수 마방진의 성립 여부
            hoochoo = 0
            nari = 0     
        # 입력 숫자의 개수가 홀수n에 대해 n x n개가 아니면 False
        if nsq != nss:
            result1 = result2 = False
            print("위 입력은 입력 숫자의 개수가 nxn개가 아닙니다.")
except ValueError:
    pass
except EOFError:
    print("EOFError가 발생했습니다.")
file.close()

unique = []
for s in sumnumList:
    if s not in unique:
        unique.append(s)

if len(sumnumList) == len(unique):
    print("중복이 없습니다.")
else:
    print("중복이 있습니다.")