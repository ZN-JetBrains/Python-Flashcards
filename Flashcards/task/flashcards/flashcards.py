def add_cards(a_dict, a_amount_cards):
    for index in range(a_amount_cards):
        term = input(f"The term for card #{index + 1}:\n")
        definition = input(f"The definition for card #{index + 1}:\n")
        a_dict[term] = definition


def play_game(a_dict):
    for key, value in a_dict.items():
        print(f"Print the definition of \"{key}\":")
        user_guess = input()

        if user_guess == value:
            print("Correct!")
        else:
            print(f"Wrong. The right answer is \"{value}\".")


def run():
    flashcard_dict = {}
    num_cards = int(input("Input the number of cards:\n"))
    add_cards(flashcard_dict, num_cards)
    play_game(flashcard_dict)


if __name__ == "__main__":
    run()
