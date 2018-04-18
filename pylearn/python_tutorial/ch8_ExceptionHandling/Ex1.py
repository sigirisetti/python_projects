def readNumber():
    while True:
        try:
            return int(input("Please enter a number: "))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


readNumber()