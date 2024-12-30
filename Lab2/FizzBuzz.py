for i in range (1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz_number")
    elif i % 3 == 0:
        print("Fizz_number")
    elif i % 5 == 0:
        print("Buzz_number")
    else:
        print(i)

#Two additionnal inputs to the programm requered
while True:
    number = int(input("Enter your number: "))
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz_number")
    elif number % 3 == 0:
        print("Fizz_number")
    elif number % 5 == 0:
        print("Buzz_number")
    else:
        print("Not a FizzBuzz_number")
    if input("Do you want to continue? (y/n)") != 'y':
        break 