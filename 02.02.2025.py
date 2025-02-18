#Number of Steps to Reduce to Zero

#Write a function solve that returns the number of steps to reduce a non-negative integer to zero. If it's even, divide by 2; if it's odd, subtract 1. Example:
#Input: 14
#Output: 6
#Explanation: 14 -> 7 -> 6 -> 3 -> 2 -> 1 -> 0 

#Make sure you return your solution, don't print!

def solve(num):
  moves = 0


  while num > 0:
      if num % 2 == 0:
        num = num / 2
        moves += 1
      else:
        num = num - 1
        moves += 1

  return moves

    
solve(14)