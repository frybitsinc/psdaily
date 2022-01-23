import sys

k, n = map(int, input().split())
lan_line = [int(sys.stdin.readline()) for _ in range(k)]
min_val = 1
max_val = max(lan_line)

while(min_val<=max_val):
    mid_val = (min_val+max_val)//2
    count = 0
    for i in lan_line:
        count += i//mid_val
    if count >= n:
        min_val = mid_val+1
    else:
        max_val = mid_val-1
print(max_val)
