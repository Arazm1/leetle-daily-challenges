# Write a function solve that returns an array of the number of 1-bits (Hamming weight) for each number from 0 to n. 

#Make sure you return your solution, don't print!

def solve(n):
    result = []


    for i in range(n+1):
        converted = bin(i).count('1')
        result.append(converted)
    return result
        

#solve(5)
