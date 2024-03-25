import sys
input = sys.stdin.readline

n = int(input())
m = int(input()) 
broken = list(map(int, input().split()))

min_count = abs(100 - n)  # 초기 최소 버튼 눌린 횟수 (100에서 N으로 바로 이동하는 경우)

for nums in range(1000001):  # 0부터 1000000까지의 숫자를 대상으로 순회
    num = str(nums)

    for i in range(len(num)):  # 숫자 num의 각 자리수를 확인
        if int(num[i]) in broken:  # 고장난 버튼이라면 중단
            break
    else:# for 루프가 완전히 돌았을 때 (고장난 버튼이 없는 경우)
        min_count = min(min_count, abs(int(num) - n) + len(num))  # 최소 횟수 갱신

print(min_count)