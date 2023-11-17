number1 = 0
number2 = 0
number3 = 0
number4 = 1

x = 1
for loop in range(10):
    for loop in range(10 - number4):
        for loop in range(10 - number4):
            for loop in range(10 - number4):
                for loop in range(10 - number4):
                    print(number1, end="")
                    print(number2, end ="")
                    print(number3, end="")
                    print(number4,",", end="")
                    number4 = number4 + x
            number3 = number3 + x
            number4 = 0
        number2 = number2 + x
        number3 = 0
        number4 = 0
    number1 = number1 + x
    number2 = 0
    number3 = 0
    number4 = 0

