# A + B - C
# https://www.acmicpc.net/problem/31403

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    # result_1
    result_1 = a + b - c

    # result_2 
    result_2 = int(str(a) + str(b)) - c

    print(result_1)
    print(result_2)

    return 

if __name__=='__main__':
    main()