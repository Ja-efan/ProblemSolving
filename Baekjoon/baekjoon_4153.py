# 직각삼각형
# https://www.acmicpc.net/problem/4153

def main():

    while True:

        input_ = list(map(int, input().split()))
        if input_ == [0,0,0]:
            break
        triangle = sorted(input_)

        if triangle[2]**2 == triangle[0]**2 + triangle[1]**2:
            print('right')      
        else:
            print('wrong')

if __name__=='__main__':
    main()