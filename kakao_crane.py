def solution(board, moves):

    # 인형을 뽑고 저장할 바구니
    bucket = []
    
    # 인형을 뽑고 사라진 개수를 저장할 바구니의 길이
    answer = []
    
    # 이동 경로 받아 오기
    for move in moves:
    
        # board의 길이를 지정
        for i in range(len(board)):
        
            # board의 길이중 i번째 안에 move-1을 선택 후 > 0 이면
            if board[i][move-1] > 0:
            
                # board의 길이중 i번째 안에 move-1의 값을 bucket에 지정
                bucket.append(board[i][move-1])
                
                # board의 길이중 i번째 안에 move-1의 값을 0으로 지정
                board[i][move-1] = 0
                
                # bucket의 마지막 값과 마지막 앞에 값이 같으면
                if bucket[-1:] == bucket[-2:-1]:
                    
                    # bucket에 같은 숫자일 때의 값 빼고 bucket의 반환 
                    bucket = bucket[:-2]
                    
                    # 몇번 터졌는지 바구니에 지정
                    answer += bucket[-1:]
                    
                break
    
    # 총 사라진 인형의 수 = 몇번 터졌는지 * 2(인형이 2개씩 한번에 터지기 때문에)
    return len(answer)*2