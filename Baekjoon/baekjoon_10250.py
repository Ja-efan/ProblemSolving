# ACM 호텔 
# https://www.acmicpc.net/problem/10250

def main():
    T = int(input())
    
    for tc in range(1, T+1):
        H, W, N = map(int, input().split())

        # N 번째 손님의 객실 호수는 N // H + 1 가 된다.
        num = N // H + 1 if N % H != 0 else N // H

        # 객실의 층 수는 H % N  
        floor = N % H if N % H != 0 else H

        if num // 10 == 0:
            room_num = str(floor) + "0" + str(num)
        else:
            room_num = str(floor) + str(num)
        
        print(room_num)

    return

if __name__=='__main__':
    main()