# 수 정렬하기 2 
# quick sort 

import sys 
inputf = sys.stdin.readline
printf = sys.stdout.write

# def split(arr, l, r):
#     pivot = arr[r]  # 가장 오른쪽 원소로 피봇팅 
#     i = l - 1
#     for j in range(l, r):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i+1], arr[r] = arr[r], arr[i+1]
#     return i + 1 

# def quicksort(arr, l, r):
#     if l < r:
#         pivot_idx = split(arr, l, r)
#         quicksort(arr, l, pivot_idx-1)
#         quicksort(arr, pivot_idx+1, r)

def main():

    N = int(inputf())
    arr = list()
    for _ in range(N):
        arr.append(int(inputf()))
    
    arr_sorted = sorted(arr)

    for i in range(N):
        printf(str(arr_sorted[i])+'\n')
    # printf(*arr_sorted, sep="\n")
    
    return

if __name__=='__main__':
    main()