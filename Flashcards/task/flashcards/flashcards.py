def add_cards(a_dict, a_amount_cards):
    for index in range(a_amount_cards):
        print(f"The term for card #{index + 1}:")
        while True:
            term = input()
            if term in a_dict:
                print(f"The term \"{term}\" already exists. Try again:")
                continue
            else:
                print(f"The definition for card #{index + 1}:")
                while True:
                    definition = input()
                    if definition in a_dict.values():
                        print(f"The definition \"{definition}\" already exists. Try again:")
                        continue
                    a_dict[term] = definition
                    break
                break


def get_key(a_dict, a_value):
    for key, value in a_dict.items():
        if value == a_value:
            return key
    return None


def set_num_cards():
    while True:
        try:
            cards = int(input("Input the number of cards:\n"))
        except ValueError:
            print("[Error]: Invalid input, not a number!")
        else:
            return cards


def play_game(a_dict):
    for key, value in a_dict.items():
        print(f"Print the definition of \"{key}\":")
        user_guess = input()

        if user_guess == value:
            print("Correct!")
        else:
            if user_guess in a_dict.values():
                other_key = get_key(a_dict, user_guess)
                print(f"Wrong. The right answer is \"{value}\", but your definition is correct for \"{other_key}\".")
            else:
                print(f"Wrong. The right answer is \"{value}\".")


def run():
    flashcard_dict = {}
    num_cards = set_num_cards()
    add_cards(flashcard_dict, num_cards)
    play_game(flashcard_dict)


if __name__ == "__main__":
    run()
