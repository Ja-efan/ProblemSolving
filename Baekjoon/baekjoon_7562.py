# 나이트의 이동 [Silver I]
# https://www.acmicpc.net/problem/7562

"""
idea : 
현재 좌표에서 한 번의 이동으로 도달할 수 있는 좌표를 모두 que에 넣는다.

"""

def main():
    directions = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]  # 나이트가 움직일 수 있는 방향 목록
    tc = int(input())
    for _ in range(tc):
        l = int(input())
        src_y, src_x = map(int, input().split())
        dst_y, dst_x = map(int, input().split())
        
        step = 0
        stack = [[src_y, src_x]]
        visited = set((src_y, src_x))
        flag = False 
        while stack:
            step += 1
            tmp_stack = []
            while stack:
                curr_y, curr_x = stack.pop()                    
                if (curr_y, curr_x) == (dst_y, dst_x):
                    flag = True 
                    step -= 1
                    break 
                for dy, dx in directions:
                    ny, nx = curr_y + dy, curr_x + dx 
                    if ny < 0 or ny >= l or nx < 0 or nx >= l:
                        continue 
                    if (ny, nx) in visited:
                        continue 
                    
                    visited.add((ny, nx))
                    tmp_stack.append([ny, nx])
            if flag: break 
            stack = tmp_stack
        
        print(step)


    return 

if __name__=='__main__':
    main()