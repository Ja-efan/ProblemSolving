# 토마토 
# https://www.acmicpc.net/problem/7569

def is_valid(M, N, H, coord:tuple, tomato_boxes):
    # print(coord)
    k, i, j = coord[0], coord[1], coord[2]
    
    # 좌표 유효성 검사 
    if k < 0 or k >= H or i < 0 or i >= N or j < 0 or j >= M:
        return False
    
    # 토마토 검사
    if tomato_boxes[k][i][j] != 0:
        return False 

    return True 


def main():
    M, N, H = map(int, input().split())

    tomato_boxes = []
    for _ in range(H):
        tomato_box = []
        for _ in range(N):
            tomato_line = list(map(int, input().split()))
            tomato_box.append(tomato_line)
        tomato_boxes.append(tomato_box)
        
    
    empty_coordinates = set()
    riped_tomato_coordinates = []
    num_of_unriped_tomatoes = 0
    # 초기 익은 토마토 좌표 확인 
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato_boxes[h][n][m] == -1:
                    empty_coordinates.add((h, m, n))
                elif tomato_boxes[h][n][m] == 1:
                    riped_tomato_coordinates.append((h, n, m))
                else: 
                    num_of_unriped_tomatoes += 1
    
    if num_of_unriped_tomatoes == 0:
        print(0)
        return
    
    directions = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]  # 상 하 우 좌 앞 뒤
    
    day = -1

    while riped_tomato_coordinates:
        day += 1
        tmp_stack = list()

        while riped_tomato_coordinates:
            tomato = riped_tomato_coordinates.pop()
            k, i, j = tomato[0], tomato[1], tomato[2]

            for dk, di, dj in directions:
                nk = k + dk 
                ni = i + di
                nj = j + dj 
                if is_valid(M, N, H, (nk, ni, nj), tomato_boxes):
                    tomato_boxes[nk][ni][nj] = 1
                    tmp_stack.append((nk, ni, nj))
                    num_of_unriped_tomatoes -= 1
        
        riped_tomato_coordinates = tmp_stack
    
    if num_of_unriped_tomatoes == 0:
        print(day)
    else:
        print(-1)
    
    return

if __name__=='__main__':
    main()