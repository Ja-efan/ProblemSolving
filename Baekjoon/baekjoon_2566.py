# 최댓값 B3
# https://www.acmicpc.net/problem/2566


def main():
    max_value = 0  # 최댓값
    max_row = -1  # 최댓값 좌표 (행)
    max_col = -1  # 최댓값 좌표 (열)
    arr = []  # 입력 배열 
    for _ in range(9):
        _input = list(map(int, input().split()))
        arr.append(_input)
    
    # 완전 탐색 
    for i in range(9):
        for j in range(9):
            if max_value <= arr[i][j]:  # if max_value < arr[i][j]: 라고 조건을 둘 경우 모든 입력이 0인 경우에 좌표가 (-1, -1) 로 나옴
                max_value = arr[i][j]  # 최댓값 변경
                max_row = i + 1  # 최댓값 좌표 변경 (행)
                max_col = j + 1  # 최댓값 좌표 변경 (열)
    
    # 결과 출력 
    print(max_value)
    print(f"{max_row} {max_col}")
    return 


if __name__ == '__main__':
    main()
