import re

def solution(s):
    
    # aa와 2a는 길이가 똑같기 문에 s <= 2 이면 s의 길이 return 
    if len(s) <= 2:
        return len(s)

    # 최종 문자열 길이를 지정할 리스트
    result_count = []

    # 문자열길이의 반절 길이만 구함
    for i in range(1, len(s)//2 + 1):

        # s에서 문자열 길이 만큼 선택해 1개의 그룹으로 묶고 space bar를 split해 문자열을 나누어줌 
        reList = re.sub('(\w{%i})' %i, '\g<1> ', s).split()

        # count 초기화
        count = 1

        # 바꿀 문자열을 저장할 리스트 지정
        result = []

        # 연속하는 문자를 판별
        for j in range(len(reList)):

            # 문자열 길이 까지만 계산 and 현재 문자와 다음 문자가 같을 때
            if j < len(reList) - 1 and reList[j] == reList[j + 1]:

                # 같은 문자이면 count += 1
                count += 1
            
            # 현재 문자와 다음 문자가 다를 때
            else:

                # 같은 문자가 없어, count = 1일 때 
                if count == 1:

                    # 현재 문자열을 append
                    result.append(reList[j])

                # 같은 문자가 있어, count != 1 일 때
                else:

                    # count 값 + 현재 문자열을 append
                    result.append(str(count) + reList[j])

                    # count 초기화 
                    count = 1
            
        # 최종 결과의 문자열 수를 세기 위해 (,)를 없앰
        result_count.append(len(''.join(result)))

    # 문자열의 최소 길이를 return
    return min(result_count)
        
                
print(solution('aaabbbccc'))