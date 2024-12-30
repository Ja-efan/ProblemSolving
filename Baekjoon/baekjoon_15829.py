# Hashing 
# https://www.acmicpc.net/problem/15829

def main():
    r = 31
    M = 1234567891
    alphabet_mapping = {chr(96 + i): i for i in range(1, 27)}

    L = int(input())
    string = input()
    sum_ = 0
    for i in range(L):

        sum_ += alphabet_mapping[(string[i])]*(r**i)

    H = sum_ % M 

    print(H)
    

    return

if __name__=='__main__':
    main()