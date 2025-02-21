#37. Count Prime Numbers

#Write a function solve that counts the number of prime numbers less than n.

#Example:
#Input: 10
#Output: 4
#Explanation: 2, 3, 5, 7 are prime numbers less than 10 

#Make sure you return your solution, don't print!


import math

class PrimeNumbers:
    def __init__(self, n):
        self.is_prime = 0
        self.n = n
        self.i = self.n - 1

    def solve(self):        
        while self.i > 1:
            for j in range(2, int(math.sqrt(self.i)) + 1):
                if self.i % j == 0:
                    break
            else:
                self.is_prime += 1
            self.i -= 1
        #print(self.is_prime)
        return self.is_prime

c = PrimeNumbers(10)
c.solve()
