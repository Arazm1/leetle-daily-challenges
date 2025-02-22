#53. Unique Paths in a Grid

#Write a function solve that returns the number of possible unique paths to reach bottom-right from top-left in an m x n grid (only moves down or right).

#Example:
#Input: 3, 7
#Output: 28 

#Make sure you return your solution, don't print!


def solve(m, n):

    #numerator
    o1 = m + n -2
    o2 = 1

    while o1 >= 1:
        o2 *= o1
        o1 -= 1
    
    #print(o2)

    #denominator

    d_r = m -1
    d_rr = 1
    while d_r >= 1:
        d_rr *= d_r
        d_r -= 1

    #print(d_rr)


    d_l = n - 1
    d_lr = 1
    while d_l >= 1:
        d_lr *= d_l
        d_l -= 1

    #print(d_lr)

    denominator = d_rr * d_lr

    result = o2 / denominator
    return result
    #print(result)


#solve(3, 7)
