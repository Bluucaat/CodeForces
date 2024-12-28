input()
nums = (list(map(int, input().split())))
officers, crimes = 0, 0
for i in range(len(nums)):
    if nums[i] > 0 or ([nums[i] < 0] and officers > 0):
        officers+=nums[i]
    elif nums[i] < 0 and officers <= 0:
            crimes+=1
print(crimes)
