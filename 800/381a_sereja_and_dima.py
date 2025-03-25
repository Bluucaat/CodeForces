amount_of_cards = int(input())
cards = list(map(int, input().split()))
player_index, p1_score, p2_score = 0, 0, 0

for i in range(amount_of_cards):
    drawn_card = cards.pop(0) if cards[0] > cards[-1] else cards.pop()
    if player_index == 0:
        p1_score += drawn_card
    elif player_index == 1:
        p2_score += drawn_card
    player_index ^= 1
print(p1_score, p2_score)