# fly me to the alpha centauri

# dynamic programming..? x
# 거리를 이용해서 풀기

tc = int(input())

for _ in range(tc):
    x, y = map(int, input().split())

    distance = y - x  # y와 x사이의 거리
    tmp = 0  # 이동 거리
    cnt = 0  # 공간 장치 이동 횟수
    moving = 0  # 반복 횟수

    while tmp < distance:
        cnt += 1
        if cnt % 2 != 0:  # 이동횟수가 짝수일 경우가 아니면 moving 1 증가
            moving += 1
        tmp += moving
    print(cnt)

# brute force 를 이용한 방식 시도
# ----------------------------------------------------------
# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# cnt_result = 10**5


# def dfs(cnt, x, y, k):
#     global cnt_result
#     if x == y:
#         cnt_result = min(cnt, cnt_result)
#         return
#     if x <= 0 or k <= 0 or cnt > cnt_result:
#         return
#     print(x, y, cnt, k)
#     dfs(cnt + 1, x + k + 1, y, k + 1)
#     dfs(cnt + 1, x + k, y, k)
#     dfs(cnt + 1, x + k - 1, y, k - 1)


# n = int(input())

# for i in range(n):
#     x, y = map(int, input().split())
#     dfs(0, x, y, 0)
#     print(cnt_result)
