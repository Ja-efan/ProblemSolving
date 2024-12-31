# 부녀회장이 될테야 
# https://www.acmicpc.net/problem/2775

def main():
    T = int(input())
    for tc in range(1, T+1):
        k = int(input())  # 층 수 
        n = int(input())  # 호 수 

        # 아파트 초기화 
        apt = [[0 for _ in range(n+1)] for _ in range(k+1)]
        for i in range(n+1):
            apt[0][i] = i

        for layer in range(1, k+1):
            for i in range(1, n+1):
                apt[layer][i] = sum(apt[layer-1][:i+1])

        print(apt[-1][-1])
    return

if __name__=='__main__':
    main()