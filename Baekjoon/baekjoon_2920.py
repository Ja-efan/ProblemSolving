# 음계 
# https://acmicpc.net/problem/2920

def main():
    
    nums = list(map(int, input().split()))

    asc = sorted(nums)
    desc = sorted(nums, reverse=True)

    if nums == asc:
        print('ascending')
    elif nums == desc:
        print('descending')
    else:
        print('mixed')
        
if __name__=='__main__':
    main()