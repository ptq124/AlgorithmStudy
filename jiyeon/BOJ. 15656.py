# n과 m (7)

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()


def brute(lst):
    if len(lst) == m:
        print(*lst, sep=" ")
        return
    for i in n_list:
        brute(lst + [i])


brute([])
