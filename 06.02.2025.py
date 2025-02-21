#37. Count Prime Numbers

#Write a function solve that counts the number of prime numbers less than n.

#Example:
#Input: 10
#Output: 4
#Explanation: 2, 3, 5, 7 are prime numbers less than 10 

#Make sure you return your solution, don't print!


import math
def solve(n):

    is_prime = 0
    i = n - 1
    
    while i > 1:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            is_prime += 1
        i -= 1
    return is_prime

#solve(11)
