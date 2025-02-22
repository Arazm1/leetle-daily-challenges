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
    print(result)


solve(3, 7)