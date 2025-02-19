class RomanConverter:
    def __init__(self):
        self.roman_map = [
            (1000, "M"), 
            (900, "CM"), 
            (500, "D"), 
            (400, "CD"),
            (100, "C"), 
            (90, "XC"), 
            (50, "L"), 
            (40, "XL"),
            (10, "X"), 
            (9, "IX"), 
            (5, "V"), 
            (4, "IV"), 
            (1, "I")
        ]
        
    def convert(self, num):
        roman_numeral = ""
        

        for value, symbol in self.roman_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        
        return roman_numeral


user_input = int(input("Enter a number you wish to convert into roman numeral: " ))

converter = RomanConverter()
result = converter.convert(user_input)
print(f"The Roman numeral for {user_input} is: {result}")
