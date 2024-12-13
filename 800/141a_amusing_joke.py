from collections import Counter

guest_name = input()
host_name = input()
pile = input()

required_letters = Counter(guest_name + host_name)
pile_letters = Counter(pile)

if required_letters == pile_letters: print("YES")
else: print("NO")