# 수 정렬하기 2 
# quick sort 

import sys 
sys.setrecursionlimit(10000)

def split(arr, l, r):
    pivot = arr[r]  # 가장 오른쪽 원소로 피봇팅 
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1 

def quicksort(arr, l, r):
    if l < r:
        pivot_idx = split(arr, l, r)
        quicksort(arr, l, pivot_idx-1)
        quicksort(arr, pivot_idx+1, r)

def main():
    N = int(sys.stdin.readline())
    arr = [0 for _ in range(N)]

    for i in range(N):
        # arr[i] = int(input())
        arr[i] = int(sys.stdin.readline())
    quicksort(arr, 0, N-1)

    print(*arr, sep="\n")
    
    return

if __name__=='__main__':
    main()