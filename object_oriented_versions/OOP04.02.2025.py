# Write a function solve that returns an array of the number of 1-bits (Hamming weight) for each number from 0 to n. 

# Make sure you return your solution, don't print!


class CountingBits:
    def __init__(self, n):
        self.n = n
        self.result = []


    def solve(self):
        for i in range(self.n + 1):
            converted = bin(i).count('1')
            self.result.append(converted)
        #print(self.result)
        return self.result

s = CountingBits(5)
s.solve()
#print(s.solve())   #Just dont use it same time with the above line
