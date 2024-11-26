magnet_count = int(input())
magnet = input()
count = 1
for i in range(magnet_count-1):
    new_magnet = input()
    if magnet != new_magnet:
        magnet = new_magnet
        count+=1
print(count)