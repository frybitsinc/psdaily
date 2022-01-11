total_sugar = int(input())
total_bag = 0
while total_sugar >= 0:
    if total_sugar%5 == 0:
        total_bag += (total_sugar//5)
        print(total_bag)
        break;
    total_sugar -= 3
    total_bag += 1
if total_sugar < 0:
    print(-1)
