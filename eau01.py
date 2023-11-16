number1 = 0
number2 = 1
number3 = 2
x = 1
for loop in range(10):
    for loop in range(10 - number2):
        for loop in range(10 - number3):
            
            print(number1, end="")
            print(number2, end="")
            print(number3,",", end="")
            number3 = number3 + x
        number2 = number2 + x
        number3 = number2 + x
    number1 = number1 + x
    number2 = number1 + x
    number3 = number2 + x
    