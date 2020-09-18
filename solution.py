import re

def solution(s):
    for i in range(1, len(s)//2 + 1):
        reList = re.sub('(\w{%i})' %i, '\g<1> ', s).split()
        count = 1
        result = []
        for j in range(len(reList)):
            if reList[j] == reList[j + 1]:
                count +=1
            else:
                if count == 1:
                    result.append(reList[j])
                else:
                    result.append(str(count) + reList[j])
                    count = 1
                
            print(reList)

solution('aabbaccc')