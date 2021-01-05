flashcard_dict = {}
term = input()
definition = input()
flashcard_dict[term] = definition

user_guess = input()

if user_guess == flashcard_dict[term]:
    print("Your answer is right!")
else:
    print("Your answer is wrong...")
