input()
game_statistics = input().strip()
anton_win_amount = game_statistics.count('A')
danik_win_amount = game_statistics.count('D')

if anton_win_amount == danik_win_amount:
    print("Friendship")
elif anton_win_amount > danik_win_amount:
    print("Anton")
else:
    print("Danik")
