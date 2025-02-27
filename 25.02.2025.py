#56. Rotate Array (Cyclic)

#Write a function solve that rotates an array to the right by k steps. Ideally, you should be able to rotate the array in-place, but be sure to still return your solution.

#Example:
#Input: [1,2,3,4,5,6,7], 3
#Output: [5,6,7,1,2,3,4] 

#Make sure you return your solution, don't print!

def solve(nums, k):


    n = len(nums)
    k = k % n

    first_array = []
    second_a = []

    for i in range(n - k):
        first_array.append(nums[i])
    
    #print(new_array)

    for j in range(n - k, n):
        second_a.append(nums[j])

    #print(reversed_a)

    result_a = second_a + first_array
    #print(result_a)
    return result_a


#solve([1,2,3,4,5,6,7], 3)