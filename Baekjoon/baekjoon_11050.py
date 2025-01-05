# 이항 계수 1
# https://www.acmicpc.net/problem/11050

# nCk = n! / r!(n-r)!

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i 

    return result


def main():
    
    N, K = map(int, input().split())
    result = factorial(N) / (factorial(K)*(factorial(N-K)))
    
    print(int(result))

if __name__=='__main__':
    main()