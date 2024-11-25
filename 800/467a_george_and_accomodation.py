room_amount = int(input())
count = 0
for i in range(room_amount):
    current_room = list(map(int, input().split()))
    if current_room[1] - current_room[0] >= 2:
        count+=1
print(count)