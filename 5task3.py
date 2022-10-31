
nums = [0, 1, 2, 3, 4, 7, 8, 10]
ranges = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
iranges = iter(nums[0:1] + ranges + nums[-1:])
print (', '.join([str(n) + '-' + str(next(iranges)) for n in iranges]))

nums = [4,7,10]
ranges = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
iranges = iter(nums[0:1] + ranges + nums[-1:])
print (', '.join([str(n) + '-' + str(next(iranges)) for n in iranges])) 

nums = [2, 3, 8, 9] 
ranges = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
iranges = iter(nums[0:1] + ranges + nums[-1:])
print (', '.join([str(n) + '-' + str(next(iranges)) for n in iranges])) 