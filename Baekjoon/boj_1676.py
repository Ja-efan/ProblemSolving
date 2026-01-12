# 팩토리얼 0의 개수 
# https://www.acmicpc.net/problem/1676

import sys 

inputf = sys.stdin.readline

def main():

    N = int(inputf())
    n_factorial = 1
    for i in range(1, N+1):
        n_factorial *= i

    cnt = 0
    n_factorial_str = str(n_factorial)
    for i in range(-1, -len(n_factorial_str), -1):
        if n_factorial_str[i] != '0':
            break
        cnt += 1
    
    print(cnt)
    return

if __name__=='__main__':
    main()