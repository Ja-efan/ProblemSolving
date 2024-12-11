# 세로읽기 B1
# https://www.acmicpc.net/problem/10798


from collections import defaultdict

def main():
    words = []  # 입력 단어 리스트 
    for i in range(5):
        words.append(input())
    
    _dict = defaultdict(str)  # 각 단어의 index 별 원소를 담을 딕셔너리 
    for row in range(5):  
        for col in range(len(words[row])):
            _dict[col] += (words[row][col])  # 현재 단어(words[row])의 현재 철자(words[row][col]을 딕셔너리에 추가 
    
    result = ''  # 출력 값 
    for _, v in _dict.items():  # 딕셔너리 아이템 순회 
        result += v

    print(result)
    return 

if __name__ == '__main__':
    main()