from itertools import combinations

card_num, target_sum = map(int, input().split())
card_list = list(map(int, input().split()))
max_sum = 0
TOTAL_CARD = 3

for cards in combinations(card_list, TOTAL_CARD):
    if max_sum < sum(cards) <= target_sum:
        max_sum = sum(cards)
print(max_sum)
