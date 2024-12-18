while True:
    try:
        num1 = int(input("What is your first Number: "))
        if num1 < 0:
            print("You need to select a positive number")
            continue
    except ValueError:
        print("The value you entered isn't a number, please enter a valid number.")
        continue
    
    try:
        num2 = int(input("What is your second Number: "))
        if num2 < 0:
            print("You need to select a positive number")
            continue
    except ValueError:
        print("The value you entered isn't a number, please enter a valid number.")
        continue

    nums = range(num1,num2)

    def is_prime(num):
        for x in range(2,num):
            if (num%x) == 0:
                return False
            else:
                return True

    primes=list(filter(is_prime, nums))
    print(primes)

    break