# 숫자의 개수 
# https://www.acmicpc.net/problem/2577

def main():
    N = 3
    num = 1
    for _ in range(N):
        num *= int(input())
    
    num2str = str(num)
    num_arr = [0 for _ in range(10)]
    for n_str in num2str:
        n = int(n_str)
        num_arr[n] += 1

    # print(*num_arr, end="\n")
    for i in num_arr:
        print(i)

    return 

if __name__=='__main__':
    main()