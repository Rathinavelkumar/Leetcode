nums = [3,2,3]
target = 6

result = {}
for i in range(len(nums)):
    temp = target-nums[i]
    if temp not in result:
        result[nums[i]] = i
    else:
        print([result[temp],i])