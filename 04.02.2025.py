def solve(n):
    result = []


    for i in range(n+1):
        converted = bin(i).count('1')
        result.append(converted)
    return result
        

solve(5)