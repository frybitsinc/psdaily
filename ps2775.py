t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    floor_zero = [x for x in range(1, num+1)]
    for k in range(floor):
        for i in range(1, num):
            floor_zero[i] += floor_zero[i-1]
    print(floor_zero[-1])
