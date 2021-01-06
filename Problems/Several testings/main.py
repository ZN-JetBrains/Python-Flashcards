def check(inp):
    if inp.isdigit():
        number = int(inp)
        if number >= 202:
            print(number)
        else:
            print("There are less than 202 apples! You cheated on me!")
    else:
        print("It is not a number!")
