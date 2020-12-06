nums=[7,8,9,6,5]

#print(nums[3])

#for i in nums:
#    print(i)

it=iter(nums)
#Method1
print(it.__next__())
print(it.__next__())
#Method2
print(next(it))

