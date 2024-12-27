# OX 퀴즈
# https://www.acmicpc.net/problem/8958

def main():
    T = int(input())

    for tc in range(1, T+1):
        quiz_result = input()

        # sol 1 
        quiz_score = 0
        pre_result = 0
        for res in quiz_result:
            if res == "O":
                pre_result += 1
                quiz_score += pre_result
            else:
                pre_result = 0
        
        print(quiz_score)

        # # sol 2 
        # score_arr = [0 for _ in range(len(quiz_result)+1)]
        # for i in range(len(quiz_result)):
        #     if quiz_result[i] == "O":
        #         if score_arr[i-1]:
        #             score_arr[i] = score_arr[i-1] + 1
        #         else:
        #             score_arr[i] = 1 
        
        # print(sum(score_arr))


    return

if __name__=='__main__':
    main()