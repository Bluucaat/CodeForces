gift_amount = int(input())
gifts = [0] * gift_amount
givers = [0 for n in range(gift_amount)]
for i in range(gift_amount):
    givers[gifts[i]-1] = i+1
print(*givers)
