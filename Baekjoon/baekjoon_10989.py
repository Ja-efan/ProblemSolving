# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

from collections import defaultdict

def main():

    # # 메모리 초과 
    # N = int(input())
    # num_dict = defaultdict(int)

    # for _ in range(N):
    #     num_dict[int(input())] += 1

    # num_dict = dict(sorted(num_dict.items(), key=lambda x: x[0]))
    
    # for k, v in num_dict.items():
    #     for _ in range(v):
    #         print(k)

    N = int(input())
    arr = [0] * 10001
    for _ in range(N):
        arr[int(input())] += 1 

    for i in range(1, len(arr)):
        if arr[i] == 0: continue
        for _ in range(arr[i]):
            print(i)

    return 
    

if __name__=='__main__':
    main()



