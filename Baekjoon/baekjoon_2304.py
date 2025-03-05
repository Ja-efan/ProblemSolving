# 250302 
# 창고 다각형 

# from collections import deque 

def main():
    N = int(input())
    pillars = []
    for _ in range(N):
        L, H = map(int, input().split())
        pillars.append((L, H))
    
    pillars.sort(key=lambda x:x[0])  # x좌표 기준으로 정렬

    # IDEA 
    # 1. 가장 높은 기둥 찾기 
    # 2. 가장 끝 기둥(왼쪽/오른쪽)을 기준으로 가장 높은 기둥 쪽으로 이동하며 면적을 누적합한다. 
    # 3. 이동 중 다음 기둥이 기준 기둥 보다 높다면 기준 기둥을 변경해준다.

    highest_pillar_height = 0  # 가장 높은 기둥 높이 
    highest_pillar_index = -1  # 가장 높은 기둥 인덱스 
    for i in range(N):
        pillar = pillars[i]
        height = pillar[1]
        if height > highest_pillar_height:
            highest_pillar_height = height 
            highest_pillar_index = i
    

    total_polygon = 0  # 창고 다각형 넓이 

    left_height = pillars[0][1]  # 왼쪽 첫 번째 기둥 높이 
    for i in range(highest_pillar_index):  # 가장 높은 기둥까지 순회 
        if left_height < pillars[i+1][1]:  # 다음 기둥의 높이가 더 높은 경우
            total_polygon += (pillars[i+1][0] - pillars[i][0]) * left_height  # 다음 기둥과 현재 기둥 사이의 면적을 구해서 누적 
            left_height = pillars[i+1][1]  # 왼쪽 기준 기둥을 다음 기둥으로 변경 

        else:  # 다음 기둥의 높이가 더 낮은 경우  (기준 기둥 변경 x)
            total_polygon += (pillars[i+1][0] - pillars[i][0]) * left_height  # 다음 기둥과 현재 기둥 사이의 면적을 구해서 누적 

    
    right_height = pillars[-1][1]  # 오른쪽 첫 번째 기둥 높이 
    for i in range(N-1, highest_pillar_index, -1):  # 가장 높은 기둥까지 순회 
        if right_height < pillars[i-1][1]:  # 다음 기둥의 높이가 더 높은 경우 
            total_polygon += (pillars[i][0] - pillars[i-1][0]) * right_height  # 다음 기둥과 현재 기둥 사이의 면적을 구해서 누적 
            right_height = pillars[i-1][1]  # 오른쪽 기준 기둥을 다음 기둥으로 변경 
        
        else:  # 다음 기둥의 높이가 더 낮은 경우 (기준 기둥 변경 x)
            total_polygon += (pillars[i][0] - pillars[i-1][0]) * right_height  # 다음 기둥과 현재 기둥 사이의 면적을 구해서 누적 


    total_polygon += highest_pillar_height  # 가장 높은 기둥 면적 더해줌 

    print(total_polygon)  # 결과 출력


    return

if __name__=='__main__':
    main()