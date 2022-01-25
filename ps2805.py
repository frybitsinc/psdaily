import sys
input = sys.stdin.readline
n, m = map(int, input().split())
list_trees = list(map(int, input().split()))
start = 0
end = max(list_trees)

while start <= end:
    mid = (start+end)//2
    sum_cut_trees = 0
    for i in list_trees:
        if i > mid:
            sum_cut_trees += i-mid
    if sum_cut_trees >= m:
        start = mid+1
    else:
        end = mid-1
print(end)
