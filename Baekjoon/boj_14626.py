# ISBN 
# 14626 

import sys 
inputf = sys.stdin.readline


def main():
    isbn = inputf().strip()

    odd = False  # 홀수번째 숫자 여부 (0부터 시작하므로 짝수번째는 False, 홀수번째는 True)

    summation = 0  # ISBN 합계

    damaged_idx = -1  # 훼손된 숫자 인덱스 (1을 곱할지, 3을 곱할지 결정)

    for i in range(len(isbn)):
        if isbn[i] == "*":  # 훼손된 숫자 
            damaged_idx = i
            pass 
        else:
            if odd:
                summation += (3*int(isbn[i]))
            else:
                summation += int(isbn[i])
        odd = not odd           

    # 훼손된 숫자가 짝수번째인지 홀수번째인지에 따라 다르게 처리
    result = 0
    if damaged_idx % 2 == 0:
        # 훼손된 숫자가 짝수번째에 있다면 
        for i in range(1, 10):
            if (summation + i) % 10 == 0:
                result = i
                break
    else:
        # 훼손된 숫자가 홀수번째에 있다면 
        for i in range(1, 10):
            if (summation + (3*i)) % 10 == 0:
                result = i
                break

    print(result)

    return

if __name__=='__main__':
    main()