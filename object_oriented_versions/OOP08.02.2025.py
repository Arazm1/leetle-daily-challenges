#39. Armstrong Number

#Write a function solve that checks if an integer is an Armstrong number (a.k.a Narcissistic number). 

#Example:
#Input: 153
#Output: True
#Explanation: 1^3 + 5^3 + 3^3 = 153 

#Make sure you return your solution, don't print!


class ArmstrongNumber:
    def __init__(self, num):
        self.num = num
        self.total = 0


    def solve(self):

        num_str = str(self.num)
        num_digits = len(num_str)

        for i in num_str:
            self.total += int(i)**num_digits
        
        if self.total == self.num:
            print("True")
            return True
        else:
            return False

armstrong = ArmstrongNumber(153)
result = armstrong.solve()
result