# 그림 
# https://www.acmicpc.net/problem/1926


def is_valid(r, c, n, m, visited):
    """유효성 검사 함수
    """
    if r < 0 or r >= n or c < 0 or c >= m or (r,c) in visited:
        return False
    return True 


def main():

    # 배열 크기 입력
    n, m = map(int, input().split())

    # 이동 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 입력 배열
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    # 방문 처리 (r,c) 튜플로 처리 
    visited = set()

    # 그림의 개수 
    num_of_draw = 0
    # 가장 넓은 그림의 그림 
    max_size = 0

    # 탐색 
    for r in range(n):
        for c in range(m):
            if (r,c) in visited:
                continue 
            if arr[r][c] == 0:
                continue 

            num_of_draw += 1  # 그림 개수 추가 (r, c)로부터 시작하는 그림
            visited.add((r, c))
            que = [(r, c)]
            size_of_draw = 0
            while que:
                size_of_draw += 1
                curr_r, curr_c = que.pop()
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    if not is_valid(nr, nc, n, m, visited):  # 유효성 검사 
                        continue 
                    if arr[nr][nc] == 0: continue  # 색칠 안 된 부분 스킵
                    # 모든 조건이 성립하는 경우 (좌표가 유효하고, 방문하지 않았으며 색칠된 부분)
                    que.append((nr, nc))  # 큐에 추가 
                    visited.add((nr, nc))  # 방문 처리 

            # 그림의 사이즈 비교 후 업데이트
            if size_of_draw > max_size:
                max_size = size_of_draw
    
    # 결과 출력 
    print(num_of_draw)
    print(max_size)
    
    return 

if __name__=='__main__':
    main()