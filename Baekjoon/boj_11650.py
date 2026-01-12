# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys 

inputf = sys.stdin.readline

def main():
    N = int(inputf())
    coors = list()
    for _ in range(N):
        coors.append(list(map(int, inputf().split())))

    coors.sort(key=lambda x: (x[0],x[1]))

    for coor in coors:
        print(f"{coor[0]} {coor[1]}")

    return

if __name__=='__main__':
    main()