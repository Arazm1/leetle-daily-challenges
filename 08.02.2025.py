#39. Armstrong Number

#Write a function solve that checks if an integer is an Armstrong number (a.k.a Narcissistic number). 

#Example:
#Input: 153
#Output: True
#Explanation: 1^3 + 5^3 + 3^3 = 153 

#Make sure you return your solution, don't print!


def solve(num):

    total = 0
    num_str = str(num)
    num_digits = len(num_str)

    for i in str(num):
        total += int(i)**num_digits
    
    if total == num:
        return True
    else:
        return False

solve(153)