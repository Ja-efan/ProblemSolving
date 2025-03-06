# 큐 

import sys 
from collections import deque

inputf = sys.stdin.readline

def main():

    que = deque([])
    
    N = int(inputf())

    for _ in range(N):
        command = inputf().split()
        
        # print(command)
        if len(command) == 2:
            num = int(command[1])
            que.append(num)
        
        else:
            command = command[0]
            if command == 'pop':
                if not len(que):
                    print(-1)
                else:
                    print(que.popleft())
            elif command == 'size':
                print(len(que))
            
            elif command == 'empty':
                if que:
                    print(0)
                else:
                    print(1)
            elif command == 'front':
                if not len(que):
                    print(-1)
                else : print(que[0])
            elif command == 'back':
                if not len(que):
                    print(-1)
                else : print(que[-1])
    return

if __name__=='__main__':
    main()