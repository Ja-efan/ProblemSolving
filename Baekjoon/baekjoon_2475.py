# 검증수 
# https://www.acmicpc.net/problem/2475

def main():
    nums = list(map(int, input().split()))
    sum_ = 0 
    for n in nums:
        sum_ += n**2
    valid_num = sum_ % 10
    print(valid_num)

    return 

if __name__=='__main__':
    main()