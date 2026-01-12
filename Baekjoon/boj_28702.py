# FizzBuzz
# https://www.acmicpc.net/problem/28702


def main():

    outputs = [input() for _ in range(3)]

    next = None 
    for i in range(3):
        if outputs[i].isdigit():
            next = int(outputs[i]) + 3 - i
            break
    
    if next % 3 == 0 and next % 5 == 0:
        print("FizzBuzz")
    elif next % 3 == 0 and next % 5 != 0:   
        print("Fizz")
    elif next % 3 != 0 and next % 5 == 0:      
        print("Buzz")
    else: 
        print(next)
    return

if __name__=='__main__':
    main()