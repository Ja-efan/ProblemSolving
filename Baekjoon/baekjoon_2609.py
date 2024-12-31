# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

def get_gcd(a, b):
    """유클리드 호제버을 사용한 최대공약수(Greatest Common Divisor) 계산 함수 

    Args:
        a (_type_): 자연수 1
        b (_type_): 자연수 2
    """
    big_one = max(a, b)
    small_one = min(a, b)
    r = 1
    while True:
    
        d, r = divmod(big_one, small_one)
        # print(d, r)
        if r == 0: 
            return small_one
            
        big_one = small_one
        small_one = r

        
def main():

    n, m = map(int, input().split())

    gcd = get_gcd(n, m)
    lcm = (n*m) // gcd  # 두 자연수의 최소공배수는 두 자연수의 곱을 최대공약수로 나눈 몫

    print(gcd)
    print(lcm)

    return

if __name__=='__main__':
    main()