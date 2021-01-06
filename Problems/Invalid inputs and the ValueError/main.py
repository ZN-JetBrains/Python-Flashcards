def check():
    try:
        user_input = int(input())
        if 25 <= user_input <= 37:
            print(user_input)
        else:
            print("Correct the error!")
    except ValueError:
        print("Correct the error!")
