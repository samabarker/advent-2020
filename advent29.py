starting_nums = [2,15,0,9,1,20]

number_spoken = []
last_spoken = []

nums = dict()
nums[1] = [1,2,3]

#30000000

for i in range(0,30000000):
    if i < len(starting_nums):
        number_spoken.append(starting_nums[i])
    else:
        previous_number = number_spoken[i-1]
        locations = []
        for i in range(0,len(number_spoken)):
            if number_spoken[i] == previous_number:
                locations.append(i)
        if len(locations) == 1:
            number_spoken.append(0)
        else:
            last = locations[-1]
            previous = locations[-2]
            number_spoken.append(last - previous)

print(number_spoken[-1])

print(nums)