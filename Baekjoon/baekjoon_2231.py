# 분해합
# https://www.acmicpc.net/problem/2231

def main():

    N = int(input())

    for i in range(1, N):
        i2str = str(i)
        decomposition_sum = i + sum([int(n) for n in i2str])
        if decomposition_sum == N:
            print(i)
            return 
    print(0)
    return 

if __name__=='__main__':
    main()