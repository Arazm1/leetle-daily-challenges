#51. Majority Element II (n/3)
#Write a function solve that finds all elements that appear more than n/3 times in an array.

#Example:
#Input: [3,2,3]
#Output: [3] 

#Make sure you return your solution, don't print!


def solve(nums):

    mp = dict()
    result = []

    length = len(nums)
    minimum = length / 3

    for i in nums:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1

    for j in mp:
        if mp[j] > minimum:
            result.append(j)
    
    return result
    #print(result)

#solve([3, 2, 3])
