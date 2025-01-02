# 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869

def main():
    A, B, V = map(int, input().split())

    # # time out
    # day = 0
    # while True:
    #     day += 1
    #     V = V - (A - B)
    #     if V <= A:
    #         day += 1
    #         break 
    
    # print(day)

    day, r = divmod(V - A, A - B)

    # 0 <= r < (A - B)

    # print(f"#1 {day} {r}")
    r += A  # A <= r < (A - B) + A 
    # print(f"#2 {day} {r}")
    if r > A:
        day += 2
    else:
        day += 1
    # print(f"#3 {day} {r}")

    print(day)

    
    return 
     

if __name__=='__main__':
    main()