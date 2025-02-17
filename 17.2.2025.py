def solve(a, b):
  number1 = int(a, 2)
  number2 = int(b, 2)

  answer = number1 + number2

  converted = bin(answer)[2:]

  return converted



    
solve("11", "1")