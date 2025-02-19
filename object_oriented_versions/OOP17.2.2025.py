class Solve:
    def __init__(self, num_a, num_b):
        self.a = num_a
        self.b = num_b


    def convert(self):
        number1 = int(self.a, 2)
        number2 = int(self.b, 2)

        answer = number1 + number2

        converted = bin(answer)[2:]

        return converted
        


a = Solve("11", "1")
result = a.convert()
print(result)