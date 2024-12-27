# 웰컴 키트 
# https://www.acmicpc.net/problem/30802

'''
티셔츠는 남아도 되지만 부족해서는 안되고 신청한 사이즈대로 나누어주어야 한다.

펜은 남거나 부족해서는 안되고 정확히 참가자 수 만큼 준비되어야 한다.
'''
def main():
    N = int(input())
    sizes = list(map(int, input().split()))
    T, P = map(int, input().split())

    num_of_tshirt_bundles = 0
    for size in sizes:
        q = size // T 
        r = size % T
        num_of_tshirt_bundles += q 
        if r: num_of_tshirt_bundles += 1
    
    print(num_of_tshirt_bundles)

    num_of_pen_bundles = N // P
    num_of_pens = N % P 
    print(num_of_pen_bundles, num_of_pens)
    
    return

if __name__=='__main__':
    main()