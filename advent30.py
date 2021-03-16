starting_nums = [2,15,0,9,1,20]

number_spoken = []
last_spoken = []

nums = dict()

#30000000

for i in range(0,30000000):
    if i < len(starting_nums):
        nums[starting_nums[i]] = [i]
        previous_number = starting_nums[i]
    else:
        if len(nums[previous_number]) == 1:
            try:
                nums[0].append(i)
            except:
                nums[0] = [i]
            previous_number = 0
        else:
            difference = nums[previous_number][-1] - nums[previous_number][-2]
            try:
                nums[difference].append(i)
            except:
                nums[difference] = [i]
            previous_number = difference
    

print(previous_number)