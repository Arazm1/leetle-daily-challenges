#53. Unique Paths in a Grid

#Write a function solve that returns the number of possible unique paths to reach bottom-right from top-left in an m x n grid (only moves down or right).

#Example:
#Input: 3, 7
#Output: 28 

#Make sure you return your solution, don't print!

class UniquePathsinaGrid:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    
    def solve(self):
        #numerator
        self.o1 = self.m + self.n -2
        self.o2 = 1

        while self.o1 >= 1:
            self.o2 *= self.o1
            self.o1 -= 1
        
        #print(o2)

        #denominator

        self.d_r = self.m -1
        self.d_rr = 1
        while self.d_r >= 1:
            self.d_rr *= self.d_r
            self.d_r -= 1

        #print(d_rr)


        self.d_l = self.n - 1
        self.d_lr = 1
        while self.d_l >= 1:
            self.d_lr *= self.d_l
            self.d_l -= 1

        #print(d_lr)

        self.denominator = self.d_rr * self.d_lr

        self.result = self.o2 / self.denominator
        return self.result

c = UniquePathsinaGrid(7, 3)
result = c.solve()
print(result)