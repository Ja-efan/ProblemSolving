# 소수 찾기 
# https://www.acmicpc.net/problem/1978

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    # print(nums)
    num_of_primes = 0
    for num in nums:
        half = num // 2
        if half < 1:
            continue 
        is_prime = True 
        for div in range(1, half+1):
            if div == 1: continue
            if num % div == 0:
                is_prime = False 
                break 
        if is_prime:
            num_of_primes += 1

    print(num_of_primes)
    return

if __name__=='__main__':
    main()
