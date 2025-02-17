#Write a function solve that adds two binary strings and returns their sum as a binary string.

#Example:
#Input: "11", "1"
#Output: "100" 

#Make sure you return your solution, don't print!

def solve(a, b):
  number1 = int(a, 2)
  number2 = int(b, 2)

  answer = number1 + number2

  converted = bin(answer)[2:]

  return converted



    
solve("11", "1")
