# 평범한 배낭 Gold V 
# https://www.acmicpc.net/problem/12865

# knapsack (DP)

def main():

    # 문제 입력 
    N, K = map(int, input().split())

    items = []
    for _ in range(N):
        w, v = map(int, input().split())
        items.append((w, v))
    
    # memoization 배열 -> (아이템 개수 x 수용 무게) 크기의 2차원 배열 생성 
    memo = [[0 for _ in range(K+1)] for _ in range(N+1)]

    # 배열 순회하면서 문제 해결 
    for i in range(1, N+1):  # i는 아이템 번호를 의미하며, items[i-1]을 넣거나 넣지 않는 경우에 대한 상황을 저장한다.
        for k in range(1, K+1):  # k는 K를 부분 문제로 정의하기 위해 필요한 부분 무게 이며, 가방을 최대 k 무게까지 채우는 경우를 저장한다.
            if items[i-1][0] > k:  # 현재 아이템(items[i-1])의 무게가 부분 무게(k)를 초과하여 가방에 넣지 못하는 경우 
                memo[i][k] = memo[i-1][k]  # 현재 아이템을 넣기 전 k 무게로 가질 수 있는 최대 가치합을 그대로 저장 -> 이전 행의 k 열에 저장된 값 
            else:  # 현재 아이템을 부분 무게 k 이하인 경우 즉, 현재 아이템을 가방에 넣을 수 있는 경우 
                # 현재 아이템을 넣었을 때 가치합(1)과 넣지 않았을 때의 가치합(2)을 비교하여 더 큰 가치합을 가지는 경우를 선택한다.
                # 1. 현재 아이템을 고려하지 않은 이전 행(i-1) 중 현재 부분 무게 k 에서 현재 아이템 무게 items[i-1][0]을 뺀 무게에 해당하는 열의 가치합에 현재 아이템의 가치를 더한다.
                # 2. 부분 무게 k 에 대해서 현재 아이템을 넣지 않은 경우 최대 가치합은 이전 아이템에 대해 무게 k까지 고려한 경우의 가치합이므로, memo[i-1][k]
                # 두 경우의 가치합 중 더 큰 값을 현재 아이템에 대해 k까지 고려한 최대 가치합으로 저장한다.
                memo[i][k] = max(memo[i-1][k-items[i-1][0]] + items[i-1][1], memo[i-1][k])
            
    print(memo[-1][-1])

    return 

if __name__=='__main__':
    main()