# 팰린드롬수
# https://www.acmicpc.net/problem/1259

def main():
    while True:
        tc = list(input())
        if tc == ['0']: break 

        # print(tc)
        # print(tc.reverse())
        # print(tc)
        reverse = tc.copy()
        reverse.reverse()
        # print(origin, tc)
        
        if tc == reverse:
            print('yes')
        else:
            print('no')
        
    return

if __name__=='__main__':
    main()