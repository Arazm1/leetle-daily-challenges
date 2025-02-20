'''
def solve(nums):
  
    result = []

    length = len(nums)
    minimum = length / 3

    for i in nums:
        if i >= minimum and i not in result:
            result.append(i)
    
    return result
    #print(result)

solve([3, 2, 3])
'''



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

solve([3, 2, 3])