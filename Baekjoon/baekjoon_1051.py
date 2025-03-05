# 숫자 정사각형 

def main():
    rec = list()
    N, M = map(int, input().split())

    MAX_SIZE = min(N, M)  # 주어진 입력에서 나올 수 있는 한 변의 최대 길이 

    for _ in range(N):
        rec.append(list(map(int, input())))  # N x M 행렬 

    for size in range(MAX_SIZE, 0, -1):  # MAX_SIZE 부터 1씩 줄여가면서 탐색

        for r in range(N-size+1):  # 현재 size를 만들 수 있는 rows  
            for c in range(M-size+1):  # 현재 size를 만들 수 있는 cols
                # (r, c): 기준좌표
                if rec[r][c] == rec[r][c+size-1] == rec[r+size-1][c] == rec[r+size-1][c+size-1]:  # 기준 좌표를 기준으로 size 만큼 떨어진 좌표들의 값을 확인 
                    result = size**2  
                    print(result)
                    return 

if __name__=='__main__':
    main()