# 수 찾기 
# https://www.acmicpc.net/problem/1920

def main():
    N = int(input())
    numbers = set(map(int, input().split()))

    M = int(input())
    find_numbers = list(map(int, input().split()))

    for fn in find_numbers:
        if fn in numbers:
            print(1)
        else:
            print(0)
                        

    return

if __name__=='__main__':
    main()