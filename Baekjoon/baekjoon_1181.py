# 단어 정렬
# https://www.acmicpc.net/problem/1181

def main():
    N = int(input())
    words = set()
    for _ in range(N):
        word = input()
        word_length = len(word)
        words.add((word, word_length))

    words_sorted = sorted(list(words), key=lambda x: (x[1], x[0]))
    # print(words_sorted)

    for word, length in words_sorted:
        print(word)


    return

if __name__=='__main__':
    main()