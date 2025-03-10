#51. Majority Element II (n/3)
#Write a function solve that finds all elements that appear more than n/3 times in an array.

#Example:
#Input: [3,2,3]
#Output: [3] 

#Make sure you return your solution, don't print!

class MajorityElementII:
    def __init__(self, nums):
        self.nums = nums
        self.mp = dict()
        self.result = []
        

    def solve(self):

        length = len(self.nums)
        minimum = length / 3

        for i in self.nums:
            if i in self.mp:
                self.mp[i] += 1
            else:
                self.mp[i] = 1

        for j in self.mp:
            if self.mp[j] > minimum:
                self.result.append(j)
        
        return self.result

m = MajorityElementII([3, 2, 3])
result = m.solve()
print(result)
