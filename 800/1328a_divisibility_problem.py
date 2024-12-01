for i in range(int(input())):
    nums = list(map(int, input().split(" ")))
    moves = nums[0]
    if nums[1] > nums[0]:
        print(nums[1] - nums[0])
    elif nums[0] % nums[1] == 0:
            print(0)
    else:
        print(nums[1] - (nums[0] % nums[1]))
