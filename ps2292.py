n = int(input())
hive_count = 1
max_hive_range = 1
if n==1:
    print(1)
else:
    while True:
        if n <= max_hive_range:
            print(hive_count)
            break
        max_hive_range += 6*hive_count
        hive_count += 1
